# Layer Masks, Channels, and Quick Mask

A layer mask is a grayscale overlay that controls a layer's transparency without erasing pixels; the Channels dialog exposes the image's color components and any saved selection masks; Quick Mask lets you paint a selection directly. This file states each direction of effect exactly as the manual does.

**When this applies:** Read this when an agent needs to add, apply, show, edit, disable, or delete a layer mask; inspect color channels; save a selection to a channel and load it back; or toggle and paint in Quick Mask.

## Layer masks and the white/black direction

Add a mask with **Layer > Mask > Add Layer Masks…**. The initialization dialog offers **White (full opacity)**, **Black (full transparency)**, **Layer's alpha channel**, **Transfer layer's alpha channel**, **Selection**, **Grayscale copy of layer**, and **Channel**.

White leaves the layer's existing alpha unchanged; black hides the layer and gray partially reduces visibility. A white mask cannot restore pixels already transparent in the layer. The **Selection** initializer uses selection coverage as the mask, preserving existing alpha where fully selected and hiding unselected areas.

```text
Apply (bake into layer): Layer > Mask > Apply Layer Masks
Show (view the mask):    Layer > Mask > Show Layer Masks    — Alt+click the mask thumbnail (green border)
Edit (paint the mask):   Layer > Mask > Edit Layer Mask     — white border on the mask thumbnail
Disable (temporarily):   Layer > Mask > Disable Layer Masks — Ctrl+Alt+click the mask thumbnail (red border)
```

## The Channels dialog

Open it from **Windows > Dockable Dialogs > Channels**. For an RGB image it lists the color channels **Red**, **Green**, **Blue**, and **Alpha** (Alpha is absent until the image has transparency); grayscale images show **Gray** and indexed images show **Indexed**.

Color channels apply to the whole image, keep a fixed order, and cannot be removed. Saved selection-mask channels are different: they store a selection as a gray-level channel, appear below the color channels, and can be created, renamed, reordered, and deleted. The dialog's bottom row includes New Channel, Raise Channels, Lower Channels, Duplicate Channels, Replace the Selection with Selected Channels, and Delete Channels.

## Saving and loading selections

```text
Save current selection to a channel:  Select > Save to Channel
Load a channel back as a selection:   "Replace the Selection with Selected Channels" button
Context-menu set operations:          Channels to Selection · Add Channels to Selection
                                       Subtract Channels from Selection · Intersect Channels with Selection
```

## Quick Mask

Quick Mask shows the unselected region as a translucent red overlay so you can refine a selection with paint tools. Toggle it with the button in the lower-left corner of the image window, the command **Select > Toggle Quick Mask**, or the shortcut **Shift+Q**. The manual frames the painting rule by the masked (covered) area, not by the selection: use white or gray to decrease the area limited by the mask, and black to increase it.

```text
Shift+Q → paint with black to grow the mask (shrink selection), white to shrink the mask (grow selection)
```

## Do / Don't

- **Do** remember the mask direction: white preserves existing alpha, black hides, gray partially masks.
- **Do** distinguish the thumbnail shortcuts: Alt+click shows the mask, Ctrl+Alt+click disables it.
- **Do** paint white to select pixels in Quick Mask, black to deselect, and gray for partial selection.
- **Don't** confuse fixed color channels (Red/Green/Blue/Alpha) with removable saved selection-mask channels.

## Related

[layers and modes](layers-and-modes.md) · [selections](selections.md) · [colors and adjustments](colors-and-adjustments.md) · [pdb recipes selections paths](pdb-recipes-selections-paths.md)
