# Python-Fu Plug-ins

Open when implementing a GIMP 3.x Python plug-in with GObject Introspection or using its Python console.

## A complete message plug-in

Save the following as `skill-message/skill-message.py` in a configured Plug-ins folder. Make it executable where required and restart GIMP. Run it with an image and drawable selected. The example adds **Filters > Tutorial > Skill Message** and reports a message without editing the image.

```python
#!/usr/bin/env python3
import sys
import gi

gi.require_version("Gimp", "3.0")
from gi.repository import Gimp


class MessagePlugin(Gimp.PlugIn):
    def do_query_procedures(self):
        return ["plug-in-skill-message-python"]

    def do_create_procedure(self, name):
        if name != "plug-in-skill-message-python":
            return None
        procedure = Gimp.ImageProcedure.new(
            self, name, Gimp.PDBProcType.PLUGIN, self.run, None
        )
        procedure.set_image_types("*")
        procedure.set_sensitivity_mask(Gimp.ProcedureSensitivityMask.DRAWABLE)
        procedure.set_menu_label("Skill Message")
        procedure.add_menu_path("<Image>/Filters/Tutorial")
        procedure.set_documentation("Show a message", "Display Hello.", name)
        procedure.set_attribution("Example author", "Example author", "2026")
        return procedure

    def run(self, procedure, run_mode, image, drawables, config, run_data):
        Gimp.message("Hello")
        return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, None)


Gimp.main(MessagePlugin.__gtype__, sys.argv)
```

The callback receives `(procedure, run_mode, image, drawables, config, run_data)`; `drawables` is a collection, not a single drawable. Query names and created procedure names must agree.

## Imports and PDB calls

Pin versioned namespaces before importing them: GIMP 3.2 still uses `gi.require_version("Gimp", "3.0")`. If a plug-in needs a GUI, also require `GimpUi` version `3.0` before importing `GimpUi`. Import `GLib` for error objects and `GObject` when declaring properties; the message example needs neither.

Typed methods such as `Gimp.Image.new(...)` and `drawable.brightness_contrast(...)` are available alongside [generic PDB lookup](pdb-reference.md#calling-from-python). A looked-up procedure takes a config object, not the positional arguments used by a typed method. Set `run-mode` only for procedures whose signatures contain that property.

## Python-Fu Console

Open **Filters > Development > Python-Fu > Python Console**. GIMP 3 preloads namespaces including `Gimp`, `Gio`, `GimpUi`, `GLib` and `GObject`. Use `Gimp.get_pdb()` to access procedures and the console's browser to inspect available calls. Do not assume GIMP 2's lowercase `gimp` and `pdb` globals exist.

Run these examples inside GIMP's connected Python environment. A system Python interpreter with PyGObject alone is not a substitute for the plug-in host.

## Related

[Installation](scripting-overview.md#installation) · [PDB reference](pdb-reference.md) · [Batch file conversion](pdb-recipes-io-batch.md) · [Script-Fu](script-fu.md)
