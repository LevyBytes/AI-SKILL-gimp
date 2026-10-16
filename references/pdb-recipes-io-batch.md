# PDB Recipes: File I/O and Batch

Open when loading, saving or exporting images programmatically, or running an isolated GIMP batch conversion.

## File argument conventions

In GIMP 3's Python API, `Gimp.file_load(run_mode, file)` takes a `Gio.File` and returns an image. `Gimp.file_save(run_mode, image, file, options)` saves XCF or exports according to the destination extension. Its currently unused `options` argument must be `None`; it does not accept a separate drawable.

Script-Fu binds file arguments to filename strings. Its return wrapping depends on the [selected dialect](script-fu.md#pdb-binding-dialects). Do not copy a C `NULL` token or a `Gio.File` object into Scheme code.

## Complete PNG-to-JPEG example

Save this block as `convert.py` beside an existing `input.png`. It requires GIMP 3's connected Python environment and installed PNG/JPEG handlers. `output.jpg` must not already exist. The loaded image is private to this job: flattening discards its layer structure and composites transparency against white, while the source file is untouched.

```python
from pathlib import Path
import gi

gi.require_version("Gimp", "3.0")
gi.require_version("Gegl", "0.4")
from gi.repository import Gimp, Gegl, Gio


def convert_png_to_jpeg(source_name, target_name):
    source = Path(source_name).resolve(strict=True)
    target = Path(target_name).resolve()
    if source == target or target.exists():
        raise FileExistsError(f"Destination must be new: {target}")
    Gegl.init(None)
    image = Gimp.file_load(
        Gimp.RunMode.NONINTERACTIVE, Gio.File.new_for_path(str(source))
    )
    if image is None:
        raise RuntimeError("GIMP could not load the source")
    try:
        Gimp.context_push()
        try:
            if not Gimp.context_set_background(Gegl.Color.new("white")):
                raise RuntimeError("GIMP could not set the background")
            if image.flatten() is None:
                raise RuntimeError("GIMP could not flatten the image")
        finally:
            Gimp.context_pop()
        saved = Gimp.file_save(
            Gimp.RunMode.NONINTERACTIVE,
            image,
            Gio.File.new_for_path(str(target)),
            None,
        )
        if not saved:
            raise RuntimeError("GIMP could not export the image")
    finally:
        image.delete()


convert_png_to_jpeg("input.png", "output.jpg")
```

The existing-file check assumes one writer; it is not an atomic filesystem reservation. A failed exporter may leave a partial destination, so inspect it before retrying. For explicit JPEG quality or metadata choices, inspect the installed JPEG export procedure and set its config rather than assuming generic save defaults.

## Run the batch

From the directory containing those files, use the installed console executable. This is POSIX-shell syntax; on Windows use the installed executable path and equivalent shell quoting. The GIMP Python batch plug-in must be available.

```bash
gimp-console-3.0 --new-instance --no-interface --quit \
  --batch-interpreter=python-fu-eval \
  --batch='exec(open("convert.py", encoding="utf-8").read())'
```

`--new-instance` creates a separate process; `--quit` closes it after the requested work. Do not use a forced PDB quit against an interactive instance. `--batch=-` reads commands from stdin. Avoid `--no-data`/`--no-fonts` for jobs that require those resources. Check the process exit status and exported file; successfully parsing the Python is not proof that a GIMP exporter ran.

## Related

[PDB and quit contracts](pdb-reference.md#keep-the-api-surfaces-distinct) · [Installation and consoles](scripting-overview.md) · [Images and layers](pdb-recipes-images-layers.md) · [Save versus export](file-formats-and-export.md)
