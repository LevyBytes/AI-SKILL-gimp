# PDB Recipes: Images and Layers

Open when creating, filling, resizing, moving or flattening images and layers through Script-Fu in GIMP 3.x.

## Create an image and retain its objects

Run this setup in the Script-Fu Console. It explicitly selects the v2 binding dialect, so `car` extracts single PDB results. `img` and `lyr` remain available for the later snippets in this file. Use a disposable image for these editing examples.

```scheme
(script-fu-use-v2)
(define img (car (gimp-image-new 640 480 RGB)))
(define lyr
  (car (gimp-layer-new img "Example layer" 640 480
                       RGB-IMAGE 100 LAYER-MODE-NORMAL)))
(gimp-image-insert-layer img lyr -1 0)
(gimp-context-push)
(gimp-context-set-background '(255 255 255))
(gimp-drawable-fill lyr FILL-BACKGROUND)
(gimp-context-pop)
(gimp-display-new img)
```

Insertion arguments are image, layer, parent and position; `-1` denotes no parent in Script-Fu. Do not mark a newly generated unsaved image clean just to suppress its save prompt. If an interactive call fails between context push/pop, restore the context with `(gimp-context-pop)` before continuing.

## Resize the canvas and a layer together

This fits the canvas to the current layer dimensions and resets their offsets to zero. Run after the setup; edit `w` and `h` when different dimensions are required.

```scheme
(let* ((w (car (gimp-drawable-get-width lyr)))
       (h (car (gimp-drawable-get-height lyr))))
  (gimp-image-resize img w h 0 0)
  (gimp-layer-resize lyr w h 0 0))
```

## Flatten inside an undo group

Flattening discards layer structure and alpha, compositing against the current background color. The returned layer replaces the old `lyr` reference so later commands do not use a removed layer. Start/end grouping makes a successful edit one undo step; if the call raises in the console, end the open group before continuing.

```scheme
(gimp-image-undo-group-start img)
(set! lyr (car (gimp-image-flatten img)))
(gimp-image-undo-group-end img)
```

## Move the current layer

```scheme
(gimp-layer-set-offsets lyr 35 35)
```

Offsets are absolute image-relative coordinates. After edits, `(gimp-displays-flush)` refreshes displays when needed. Before duplicating, merging down, reordering, or setting opacity/mode, look up the exact installed procedure in **Help > Procedure Browser**; menu names alone are not signatures.

These console recipes deliberately use v2 return wrapping. For a new v3 plug-in, read the [dialect rules](script-fu.md#pdb-binding-dialects), switch inside the run function and remove the single-result wrappers consistently.

## Related

[Selections and paths](pdb-recipes-selections-paths.md) · [File I/O](pdb-recipes-io-batch.md) · [PDB lookup](pdb-reference.md) · [Layer concepts](layers-and-modes.md)
