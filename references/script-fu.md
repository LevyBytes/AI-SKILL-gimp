# Script-Fu Language Essentials

Open when writing Scheme expressions, selecting a PDB binding dialect, or registering Script-Fu procedures and menus in GIMP 3.x.

## Scheme syntax

Calls use parenthesized prefix notation. Bind locals with `let*`, assign with `set!`, and define variables or functions with `define`. `car` and `cdr` select a list's head and tail; quoting prevents evaluation of a literal list.

```scheme
(let* ((sum (+ 5 6))) (car '("a" "b")))   ; → "a"
```

## PDB binding dialects

GIMP 3's Script-Fu starts in the v2 binding dialect, including in the console. A single PDB result is wrapped in a list there; `car` extracts it. The optional v3 dialect returns single values directly and represents returned booleans as `#t` or `#f`. Multiple return values still require their documented structure.

Enable v3 at the beginning of a plug-in's run function, not at registration time. This complete helper returns a new image ID; the caller owns displaying or deleting the image:

```scheme
(define (make-example-image)
  (script-fu-use-v3)
  (gimp-image-new 640 480 RGB))
```

The dialect affects subsequent PDB calls in the interpreter, not just one lexical function. Avoid mixing v2 helpers with v3 callers without an explicit dialect boundary. GIMP 3's array arguments use vectors without a separate array-length argument, independently of the chosen return-value dialect.

## Register a standalone filter

Save this complete example as `skill-message/skill-message.scm` in a configured Plug-ins folder. Make it executable where required and restart GIMP. It needs an open image with at least one selected drawable and adds a Tutorial menu command that displays a message.

```scheme
#!/usr/bin/env gimp-script-fu-interpreter-3.0

(define (plug-in-skill-message image drawables text)
  (script-fu-use-v3)
  (gimp-message text))

(script-fu-register-filter
  "plug-in-skill-message"
  "Skill Message"
  "Display the supplied message."
  "Example author"
  "Example author"
  "2026"
  "*"
  SF-ONE-OR-MORE-DRAWABLE
  SF-STRING "Message" "Hello")
(script-fu-menu-register "plug-in-skill-message" "<Image>/Filters/Tutorial")
```

`script-fu-register-filter` supplies the image and drawables to the run function; do not add those as `SF-IMAGE`/`SF-DRAWABLE` parameter triplets. Use `script-fu-register-procedure` for procedures that do not operate as image filters. These registration functions provide generated dialogs and saved settings for declared inputs.

Classic `script-fu-register` is a compatibility interface. Its leading arguments are name, label, description, author, copyright, date and image types, followed by `SF-TYPE`, label and default triplets. Do not apply that signature to the newer registration functions.

## Input and capability constants

- Object inputs include `SF-IMAGE`, `SF-LAYER`, `SF-CHANNEL`, `SF-DRAWABLE` and `SF-VECTORS`.
- Resource inputs include `SF-BRUSH`, `SF-FONT`, `SF-GRADIENT`, `SF-PALETTE` and `SF-PATTERN`.
- Value inputs include `SF-STRING`, `SF-ADJUSTMENT`, `SF-TOGGLE`, `SF-COLOR`, `SF-OPTION` and `SF-ENUM`. Use these instead of obsolete `SF-VALUE`.
- `SF-SPINNER` selects the widget inside an `SF-ADJUSTMENT` default list, such as `(list 50 1 1000 1 10 0 SF-SPINNER)`; it is not a standalone input type.
- `SF-ONE-DRAWABLE`, `SF-ONE-OR-MORE-DRAWABLE` and `SF-TWO-OR-MORE-DRAWABLE` declare filter drawable requirements.

## Related

[Installation and consoles](scripting-overview.md) · [PDB lookup](pdb-reference.md) · [Image recipes](pdb-recipes-images-layers.md) · [Selection recipes](pdb-recipes-selections-paths.md)
