#!/usr/bin/env python3
"""Convert one image to a new JPEG through a headless GIMP 3.2 batch run.

Run it with Python 3.8 or later outside GIMP. It starts gimp-console-3.2 as a separate instance, runs this same file
inside GIMP's python-fu-eval batch interpreter, flattens the image onto a white background and exports the JPEG.
The source file is never modified and an existing destination is refused, so repeating a run changes nothing.
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

JOB = "GIMP_CONVERT_TO_JPEG_JOB"
CONSOLE = "gimp-console-3.2"
LOG_LINES = 20
LOG_WIDTH = 300


def convert_inside_gimp(source, target):
    """Load, flatten onto white and export, with GIMP's own Python bindings."""
    import gi

    gi.require_version("Gimp", "3.0")
    gi.require_version("Gegl", "0.4")
    from gi.repository import Gegl, Gimp, Gio

    if target.exists():
        raise FileExistsError(f"destination already exists: {target}")
    Gegl.init(None)
    image = Gimp.file_load(Gimp.RunMode.NONINTERACTIVE, Gio.File.new_for_path(str(source)))
    if image is None:
        raise RuntimeError(f"GIMP could not load {source}")
    try:
        Gimp.context_push()
        try:
            if not Gimp.context_set_background(Gegl.Color.new("white")):
                raise RuntimeError("GIMP could not set the background color to white")
            if image.flatten() is None:
                raise RuntimeError("GIMP could not flatten the image")
        finally:
            Gimp.context_pop()
        if not Gimp.file_save(Gimp.RunMode.NONINTERACTIVE, image, Gio.File.new_for_path(str(target)), None):
            raise RuntimeError(f"GIMP could not export {target}")
    finally:
        image.delete()


def run_inside_gimp(job_text):
    """The batch-interpreter side: do the job and leave its outcome in the result file the launcher named."""
    job = json.loads(job_text)
    outcome = {"status": "ok"}
    try:
        convert_inside_gimp(Path(job["source"]), Path(job["target"]))
    except Exception as error:
        outcome = {"status": "error", "error": f"{type(error).__name__}: {error}"}
        raise
    finally:
        Path(job["result"]).write_text(json.dumps(outcome), encoding="utf-8")


def fail(what, expected, attempt, **details):
    """Report a failure as one JSON object on stdout and one line on stderr, then exit 1."""
    print(json.dumps({"status": "error", "error": what, "expected": expected, "try": attempt, **details}, ensure_ascii=False))
    print(f"convert_to_jpeg: {what} Expected: {expected} Try: {attempt}", file=sys.stderr)
    sys.exit(1)


def tail(text):
    return [line[:LOG_WIDTH] for line in text.splitlines() if line.strip()][-LOG_LINES:]


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Convert one image to a new JPEG with a headless GIMP 3.2 instance. The image is flattened onto "
                    "white, so transparency becomes white; the source file is not modified.",
        epilog="Output: one JSON object on stdout, {\"status\": \"ok\", \"source\", \"target\", \"bytes\"} on success or "
               "{\"status\": \"error\", \"error\", \"expected\", \"try\"} with exit status 1 on failure. "
               "Requires GIMP 3.2 with its Python plug-ins; set --gimp-console or GIMP_CONSOLE when "
               f"{CONSOLE} is not on PATH.")
    parser.add_argument("source", help="existing image GIMP can load, such as a PNG")
    parser.add_argument("target", help="new .jpg or .jpeg path; refused if it already exists")
    parser.add_argument("--gimp-console", default=os.environ.get("GIMP_CONSOLE", CONSOLE),
                        help=f"GIMP console executable name or path (default: $GIMP_CONSOLE or {CONSOLE})")
    parser.add_argument("--timeout", type=float, default=300, help="seconds to wait for GIMP (default: 300)")
    args = parser.parse_args(argv)

    source = Path(args.source).expanduser().resolve()
    target = Path(args.target).expanduser().resolve()
    if not source.is_file():
        fail(f"source not found: {source}", "an existing image file", "check the path and pass the image file itself")
    if target.suffix.lower() not in (".jpg", ".jpeg"):
        fail(f"target is not a JPEG path: {target}", "a target ending in .jpg or .jpeg", "rename the target")
    if target == source or target.exists():
        fail(f"target already exists: {target}", "a new destination path", "choose another target or remove the old file")
    if not target.parent.is_dir():
        fail(f"target folder not found: {target.parent}", "an existing destination folder", "create the folder first")
    console = shutil.which(args.gimp_console)
    if console is None:
        fail(f"GIMP console not found: {args.gimp_console}", f"GIMP 3.2's {CONSOLE} on PATH or a path to it",
             "install GIMP 3.2, or pass --gimp-console with the console executable's full path")

    with tempfile.TemporaryDirectory(prefix="gimp-jpeg-") as scratch:
        result_path = Path(scratch) / "result.json"
        job = {"source": str(source), "target": str(target), "result": str(result_path)}
        script = str(Path(__file__).resolve())
        code = f"exec(compile(open({script!r}, encoding='utf-8').read(), {script!r}, 'exec'))"
        command = [console, "--new-instance", "--no-interface", "--quit",
                   "--batch-interpreter=python-fu-eval", f"--batch={code}"]
        try:
            run = subprocess.run(command, env=dict(os.environ, **{JOB: json.dumps(job)}), stdin=subprocess.DEVNULL,
                                 capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=args.timeout)
        except subprocess.TimeoutExpired:
            fail(f"GIMP did not finish within {args.timeout:g} seconds", "a batch run that exits on its own",
                 "raise --timeout, or check that no dialog or crashed instance is blocking GIMP")
        log = tail(run.stdout + "\n" + run.stderr)
        outcome = json.loads(result_path.read_text(encoding="utf-8")) if result_path.is_file() else None

    if outcome is None:
        fail("GIMP exited without running the conversion", "the python-fu-eval batch interpreter to run this script",
             "check that GIMP's Python plug-ins are installed and enabled", gimp_exit=run.returncode, gimp_log=log)
    if outcome["status"] != "ok":
        fail(outcome["error"], "GIMP to load, flatten and export the image",
             "read gimp_log, and open the source in GIMP to confirm it loads", gimp_exit=run.returncode, gimp_log=log)
    if not target.is_file() or target.stat().st_size == 0:
        fail(f"GIMP reported success but wrote no JPEG: {target}", "a non-empty JPEG at the target",
             "check that GIMP's JPEG export plug-in is installed", gimp_exit=run.returncode, gimp_log=log)
    print(json.dumps({"status": "ok", "source": str(source), "target": str(target), "bytes": target.stat().st_size},
                     ensure_ascii=False))


if __name__ == "__main__":
    if os.environ.get(JOB) is not None:
        run_inside_gimp(os.environ[JOB])
    else:
        main()
