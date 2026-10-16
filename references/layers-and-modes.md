# Layers and Layer Modes

GIMP composites an image from a stack of layers, and the blend mode chosen for each layer governs how its pixels combine with everything beneath it. This file is the reference for the layer stack, layer attributes, and the full set of mode names.

**When this applies:** Read this when an agent needs to create, reorder, merge, or anchor layers, set a layer's opacity or visibility, work with layer groups or the alpha channel, or pick a layer/paint blend mode by its exact name.

## The layer stack and the Layers dialog

The image is a stack of layers: the lowest entry is the background and later entries sit in front. Open the dialog from **Windows > Dockable Dialogs > Layers** (shortcut **Ctrl+L**). Each row shows a thumbnail, an editable name (double-click to rename, or right-click and choose **Edit Layer Attributes**), and an eye toggle for visibility. The dialog header carries a **Mode** drop-down and an **Opacity** slider, plus lock controls labeled **Lock pixels**, **Lock position and size**, **Lock visibility**, and **Lock alpha channel**.

```text
Opacity range: 0 to 100 (0 = complete transparency, 100 = complete opacity)
Hide every layer except one: Shift-click that layer's eye symbol
```

## Attributes, alpha, and anchoring

Transparency is stored in a layer's alpha channel; a background layer usually has none until you add one via **Layer > Transparency > Add an Alpha Channel**. **Edit > Paste** (**Ctrl+V**) creates new layers in GIMP 3.2. Use **Edit > Paste as > Floating Data** when a temporary floating layer (floating selection) is wanted; **Layer > Anchor Floating Layer or Mask** (**Ctrl+H**) fixes it onto the previously active layer.

```text
New layer:            Layer > New Layer…            (Shift+Ctrl+N)
Duplicate:            Layer > Duplicate Layers
Merge one step down:  Layer > Merge Down
Merge all visible:    Image > Merge Visible Layers   (Ctrl+M)
Flatten everything:   Image > Flatten Image
```

## Layer groups

Create a group with **Layer > New Layer Group**, or the button at the foot of the Layers dialog. Drag layers into it, or add fresh ones with **Layer > New Layer…** while the group is active. A group set to Normal is blended as a single merged layer, whereas **Pass through** renders the group's layers in combination with the layers below the group.

## Layer modes (blend modes)

The default modes are split into seven groups: **Normal**, **Lighten**, **Darken**, **Contrast**, **Inversion**, **HSV components**, and **LCh components**. The **Normal** group contains **Normal**, **Dissolve**, **Color Erase**, **Erase**, **Merge**, and **Split**. **Pass through** is offered only for group layers.

A separate set of legacy layer modes exists for backward compatibility. Reach them with the reset icon beside the **Mode** drop-down, switching from Default to Legacy; each then shows `(legacy)` after its name.

```text
Legacy modes by group (verbatim):
  Normal:    Normal, Dissolve
  Lighten:   Lighten only, Screen, Dodge, Addition
  Darken:    Darken only, Multiply, Burn
  Contrast:  Overlay, Soft light, Hard light
  Inversion: Difference, Subtract, Grain extract, Grain merge, Divide
  HSV:       HSV Hue, HSV Saturation, HSL Color, HSV Value
```

TODO: the default (non-legacy) member names for the Lighten/Darken/Contrast/Inversion/HSV/LCh groups are not enumerated on the layer-modes overview page; only the Normal group is listed there.

## Do / Don't

- **Do** open the dialog with **Ctrl+L** and set blend behavior through the header **Mode** drop-down and **Opacity** slider.
- **Do** treat **Pass through** as a group-only mode, distinct from Normal.
- **Don't** rename a mode: the spelling and casing above (for example **Lighten only**, **Soft light**, **HSL Color**) are exact.
- **Don't** flatten when you still need separate layers; flattening discards transparency and layer structure.

## Related

[masks and channels](masks-and-channels.md) · [selections](selections.md) · [interface and workflow](interface-and-workflow.md) · [pdb recipes images layers](pdb-recipes-images-layers.md)
