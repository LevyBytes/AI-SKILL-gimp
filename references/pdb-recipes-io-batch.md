# PDB Recipes: File I/O and Batch

Open when loading, saving or exporting images programmatically, or running an isolated GIMP batch conversion.

## File argument conventions

In GIMP 3's Python API, `Gimp.file_load(run_mode, file)` takes a `Gio.File` and returns an image. `Gimp.file_save(run_mode, image, file, options)` saves XCF or exports according to the destination extension. Its currently unused `options` argument must be `None`; it does not accept a separate drawable.

Script-Fu binds file arguments to filename strings. Its return wrapping depends on the [selected dialect](script-fu.md#pdb-binding-dialects). Do not copy a C `NULL` token or a `Gio.File` object into Scheme code.

## Convert an image to JPEG

Run [`scripts/convert_to_jpeg.py`](../scripts/convert_to_jpeg.py) when one image must become a new JPEG without opening GIMP. Launch it with Python 3.8 or later from the skill root; it starts `gimp-console-3.2` as a separate instance and does the work inside GIMP's Python batch interpreter:

```bash
python scripts/convert_to_jpeg.py input.png output.jpg
```

The script loads the source with `Gimp.file_load`, pushes a context with a white background, flattens the image, exports it with `Gimp.file_save` and deletes the in-memory image. Flattening discards the layer structure and composites transparency against white; the source file is never modified. An existing target is refused, so repeating a run changes nothing. It prints one JSON object: `status`, `source`, `target` and `bytes` on success, or `error`, `expected`, `try` and the last GIMP log lines with exit status 1. Pass `--gimp-console` or set `GIMP_CONSOLE` when `gimp-console-3.2` is not on `PATH`.

The existing-target check assumes one writer; it is not an atomic filesystem reservation. A failed export may leave a partial destination, so inspect or remove it before retrying. The script uses the JPEG exporter's default settings; for explicit quality or metadata, inspect the installed JPEG export procedure and set its config.

## Run a custom batch job

Other Python batch work runs the same way: save it as a file and pass it to the console's Python batch interpreter. This is POSIX-shell syntax; on Windows use the installed executable path and equivalent quoting. The GIMP Python batch plug-in must be available.

```bash
gimp-console-3.2 --new-instance --no-interface --quit \
  --batch-interpreter=python-fu-eval \
  --batch='exec(open("job.py", encoding="utf-8").read())'
```

`--new-instance` creates a separate process; `--quit` closes it after the requested work. Do not use a forced PDB quit against an interactive instance. `--batch=-` reads commands from stdin. Avoid `--no-data`/`--no-fonts` for jobs that require those resources. Check the process exit status and exported file; successfully parsing the Python is not proof that a GIMP exporter ran.

## Related

[PDB and quit contracts](pdb-reference.md#keep-the-api-surfaces-distinct) · [Installation and consoles](scripting-overview.md) · [Images and layers](pdb-recipes-images-layers.md) · [Save versus export](file-formats-and-export.md)
