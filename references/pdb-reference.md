# The Procedural Database (PDB)

Open when looking up a GIMP procedure, checking its arguments and return values, or choosing between Script-Fu and typed Python calls.

## Discover the installed contract

**Help > Procedure Browser** searches registered procedures by name, description, help, authors, copyright, date or type. It shows the installed parameters and results, including procedures supplied by plug-ins. Availability depends on the installation.

The PDB exposes application operations to plug-ins. Script-Fu binds directly to it; Python also exposes typed libgimp methods. C helper functions and PDB procedures are not interchangeable merely because their names look alike. For example, `gimp-image-new` corresponds to `Gimp.Image.new`, but not every C helper has a same-named PDB procedure with the same signature.

## Calling from Script-Fu

In the default v2 binding dialect, this expression extracts the returned image ID:

```scheme
(car (gimp-image-new 640 480 RGB))
```

In v3, select `(script-fu-use-v3)` inside the run function and use the returned image directly. See [Script-Fu dialects](script-fu.md#pdb-binding-dialects). For GIMP 3 array inputs, pass the vector without copying the C API's separate element-count parameter.

## Calling from Python

This complete helper runs inside GIMP's Python environment. Supply an existing `Gimp.Image`. It raises on missing procedures or failed execution and returns the successful result array for the caller to inspect using the procedure's documented outputs.

```python
import gi

gi.require_version("Gimp", "3.0")
from gi.repository import Gimp


def flatten_via_pdb(image):
    procedure = Gimp.get_pdb().lookup_procedure("gimp-image-flatten")
    if procedure is None:
        raise RuntimeError("gimp-image-flatten is unavailable")
    config = procedure.create_config()
    config.set_property("image", image)
    result = procedure.run(config)
    status = result.index(0)
    if status != Gimp.PDBStatusType.SUCCESS:
        raise RuntimeError(f"gimp-image-flatten failed: {status}")
    return result
```

Use enum value equality when checking the status. Do not add `run-mode` to an internal procedure that lacks that argument. The typed alternative `image.flatten()` returns the resulting layer; its return contract differs from the generic PDB result array.

## Keep the API surfaces distinct

- `Gimp.file_save(run_mode, image, file, options)` saves/exports the whole image. `file` is a `Gio.File`; currently `options` must be `None`. Use the complete [batch recipe](pdb-recipes-io-batch.md).
- The PDB procedure `gimp-quit` takes a force boolean and requests termination of the main application. In contrast, libgimp's `Gimp.quit()`/`gimp_quit(void)` terminates a plug-in's connection and is deprecated; plug-ins should return normally. For an isolated batch invocation, use the executable's `--quit` option.
- GIMP 3 procedures such as `gimp-drawable-brightness-contrast` differ from 2.10 names. Check the actual browser signature before porting an example.

## Related

[Script-Fu](script-fu.md) · [Python plug-ins](python-fu.md) · [Images and layers](pdb-recipes-images-layers.md) · [Colors and filters](pdb-recipes-color-filters.md)
