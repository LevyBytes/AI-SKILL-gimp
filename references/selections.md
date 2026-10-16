# Selections

A selection marks which pixels of an image GIMP operations will affect; it can be all-or-nothing or a soft, partial mask where each pixel is selected by some amount.

**When this applies:** Read this when an agent needs to constrain edits to part of an image, combine selection regions, soften selection edges, or drive the **Select** menu commands.

## What a selection is

Every image carries one selection, and most operations act only on its selected portions. Selection coverage is a mask from unselected to fully selected. An 8-bit illustration uses 0 to 255; this is not a claim that every image precision stores the selection in 8 bits. This is why a selection can be *partial*: edges can fade smoothly. The moving dashed outline ("marching ants") is only a contour separating pixels that are more than half selected from those less than half selected — it cannot show partial values directly.

```text
pixel value 0   = unselected (edit does nothing here)
pixel value 128 = ~half selected (edit applied at ~50% strength)
pixel value 255 = fully selected (full-strength edit)
```

## Selection tool modes

The selection tools share a **Mode** option with four entries that decide how a new shape combines with the existing selection: **Replace**, **Add**, **Subtract**, and **Intersect**. Modifier keys held while dragging switch modes on the fly (for example **Shift** to add, **Ctrl** to subtract). The interactive tools include **Rectangle Select**, **Ellipse Select**, **Free Select (the Lasso)**, **Fuzzy Select**, **By Color Select**, **Scissors Select**, and **Foreground Select**.

```text
Mode = Add        → new shape is unioned with current selection
Mode = Subtract   → new shape is removed from current selection
Mode = Intersect  → keep only the overlap of both
```

## Feathering and anti-aliasing

By default the basic tools produce sharp-edged selections. The **Feather Edges** tool option blurs the boundary so the selection grades in and out over a feather radius (mechanically a Gaussian blur of the selection channel). The **Antialiasing** option smooths stair-stepping along curved or diagonal edges. You can also feather afterward with **Select > Feather**, which opens **Feather Selection** (field **Feather selection by**, in pixels).

## The Select menu

The **Select** menu lists, in order: **Select All** (Ctrl+A), **None** (Shift+Ctrl+A), **Invert** (Ctrl+I), **Float**, **By Color**, **Selection From Paths**, **Selection Editor**, **Feather**, **Sharpen**, **Shrink**, **Grow**, **Border**, **Remove Holes**, **Distort**, **Rounded Rectangle**, **Toggle Quick Mask**, **Save to Channel**, and **To Path**. A floating selection (from **Float**) is a temporary layer that must be anchored before working on other layers. **Select > Grow…** opens **Grow Selection** (field **Grow selection by**, pixels); **Select > To Path** converts the current selection into a path.

```text
Sharp circular selection, then Select > Feather… (e.g. 8 px)
→ edge fades over ~8 px so a fill or filter blends instead of hard-clipping
```

## Do / Don't

- **Do** set **Mode** (or hold a modifier) before dragging when building a compound selection.
- **Do** use **Select > Feather…** or **Feather Edges** when you need soft transitions.
- **Don't** confuse the marching-ants outline with the real mask — partial/feathered selection is invisible there; check via **Toggle Quick Mask**.
- **Don't** assume **Antialiasing** and **Feather Edges** are the same; anti-aliasing only smooths jaggies, feathering widens a graded transition.

## Related

[masks and channels](masks-and-channels.md) · [paths](paths.md) · [tools overview](tools-overview.md) · [pdb recipes selections paths](pdb-recipes-selections-paths.md)
