# Scripting and Plug-ins

Open when choosing a GIMP automation language, installing plug-ins, using consoles, or configuring batch execution.

## Choose an execution environment

GIMP 3.2 uses the GIMP 3.0 plug-in API and typelib names. Script-Fu binds Scheme to the PDB; Python plug-ins use Python 3 and GObject Introspection. Ordinary system Python does not provide a connected GIMP session just by importing `gi`.

Plug-ins run under GIMP's control. The Filters menu also contains GEGL operations and built-in commands; a menu entry is not proof that a same-named PDB procedure exists. Use **Help > Procedure Browser** for installed procedure signatures and the API documentation for typed methods.

For a server or MCP integration, establish which language and GIMP instance the server actually controls. This skill does not bundle an MCP server.

## Interactive consoles

- **Filters > Development > Script-Fu > Script-Fu Console** evaluates Scheme. It starts in the v2 binding dialect even in GIMP 3; [Script-Fu essentials](script-fu.md) explains the optional v3 dialect.
- **Filters > Development > Script-Fu > Start Server** starts the Script-Fu server.
- **Filters > Development > Python-Fu > Python Console** provides namespaces such as `Gimp` and `Gio`. Obtain the PDB with `Gimp.get_pdb()`; GIMP 2's `gimp` and `pdb` console globals are not the 3.x interface.

The following expression assumes the Script-Fu console's default v2 dialect and returns a new image ID without displaying it:

```scheme
(car (gimp-image-new 640 480 RGB))
```

## Installation

Inspect **Preferences > Folders > Plug-ins** for the installation's actual search paths. Place a Python or standalone Script-Fu plug-in inside a directory matching its filename stem, such as `hello/hello.py` or `hello/hello.scm`. On Unix-like systems make that file executable, then restart GIMP. The interpreter named in its shebang must be available to GIMP.

Standalone Script-Fu uses `gimp-script-fu-interpreter-3.0`, including with GIMP 3.2. Legacy extension scripts instead use **Preferences > Folders > Scripts**. Do not infer a `gimp-3.2` profile path or compiler-tool name from the application's minor version.

## Batch execution

Choose the installed executable; `gimp-console-3.0` is the console build where provided. On Windows supply its installed executable path using the invoking shell's quoting rules. This POSIX-shell example requires the Script-Fu batch interpreter:

```bash
gimp-console-3.0 --new-instance --no-interface --quit \
  --batch-interpreter=plug-in-script-fu-eval \
  --batch='(gimp-message "Batch ready")'
```

`--new-instance` isolates the batch from an already running interactive session. `--quit` exits that instance after processing. Specify `--batch-interpreter` rather than depending on an installation's default. `--batch=-` reads commands from standard input. `--no-data` and `--no-fonts` skip resources; use them only when the job does not need those resources.

For a complete load/flatten/export example and cleanup, open [File I/O and batch](pdb-recipes-io-batch.md). Check the actual installed GIMP version, procedures and dependencies before running automation; syntax checks alone do not establish native execution.

## Related

[PDB lookup](pdb-reference.md) · [Script-Fu](script-fu.md) · [Python plug-ins](python-fu.md) · [Images and layers](pdb-recipes-images-layers.md)
