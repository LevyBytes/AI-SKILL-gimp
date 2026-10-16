# PDB Recipes: Colors and Filters

Open when automating tonal adjustments or locating a filter's callable contract in GIMP 3.x.

## Drawable prerequisites

The following examples require an existing drawable ID called `drawable`, such as `lyr` from [image setup](pdb-recipes-images-layers.md). They are independent editing examples; do not run all of them as a single desired effect. Check the installed Procedure Browser for mode, channel and selection constraints.

## Tone and color signatures

These are schematic calls: bind the named parameters before execution. The `gimp-drawable-*` procedures operate on a drawable, not the whole image object.

```scheme
(gimp-drawable-brightness-contrast drawable brightness contrast)
(gimp-drawable-levels drawable channel low-in high-in clamp-in
                      gamma low-out high-out clamp-out)
(gimp-drawable-desaturate drawable desaturate-mode)
(gimp-drawable-threshold drawable channel low high)
(gimp-drawable-invert drawable linear)
```

Brightness and contrast use the range -1.0 to 1.0. Threshold bounds use 0.0 to 1.0. `channel` is a histogram-channel enum; `desaturate-mode` is a `DESATURATE-*` constant. `clamp-in`, `clamp-out` and `linear` are boolean controls. Match the [Script-Fu dialect](script-fu.md#pdb-binding-dialects) when supplying or interpreting booleans.

## Explicit curves use a vector

GIMP 3 Script-Fu passes the sample vector alone; the C API's array count is not a separate PDB argument. This example builds an identity curve of 256 floating-point values in the range 0.0 to 1.0 and applies it to `HISTOGRAM-VALUE`:

```scheme
(let ((values (make-vector 256 0.0)))
  (do ((i 0 (+ i 1)))
      ((= i 256))
    (vector-set! values i (/ i 255.0)))
  (gimp-drawable-curves-explicit drawable HISTOGRAM-VALUE values))
```

Other adjustment procedures include `gimp-drawable-curves-spline`, `gimp-drawable-equalize`, `gimp-drawable-hue-saturation`, `gimp-drawable-color-balance` and `gimp-drawable-posterize`; inspect each signature before calling it.

## Filters and Python equivalents

A GEGL operation need not have a `plug-in-*` PDB wrapper. Check the Procedure Browser for registered procedures and the GEGL operation/API documentation for operations that have no wrapper. Do not invent `gimp-drawable-hue-chroma` from the **Colors > Hue Chroma** menu label.

Typed Python methods include `drawable.brightness_contrast(...)`, `drawable.levels(...)`, `drawable.curves_explicit(...)`, `drawable.desaturate(...)` and `drawable.threshold(...)`. GObject Introspection may hide C array-length parameters too; consult the Python method's help instead of mechanically translating a C signature.

## Related

[Images and layers](pdb-recipes-images-layers.md) · [Selection recipes](pdb-recipes-selections-paths.md) · [Colors](colors-and-adjustments.md) · [Filters](filters.md) · [PDB lookup](pdb-reference.md)
