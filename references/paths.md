# Paths

Paths are editable Bézier curves you can shape precisely, then convert into selections, stroke with a tool, fill, or save as SVG.

**When this applies:** Read this when an agent needs to draw or edit a vector path, turn a path into a selection (or vice versa), stroke/outline a path, or import/export path geometry as SVG.

## What a path is

A path is a curve made of Bézier segments and can be open or closed. Each segment runs between two anchor points, drawn as black squares. A selected anchor shows two open-square handles whose direction lines control how the curve leaves the anchor before bending toward the next point. One image can hold several named paths, managed in the **Paths** dialog.

## The Paths tool

Activate from **Tools > Paths**, the toolbox icon, or shortcut **B**. With **Paths Edit Mode** set to **Design**, left-click to place the first anchor, then keep clicking to add connected anchors. To bend a segment, left-click-drag it. To close the path, click the existing anchor you want to connect back to.

```text
B (Paths tool) → click, click, click  = open path with straight segments
drag a segment                          = pull it into a curve
click back on the first anchor          = close the path
```

## The Paths dialog

The bottom buttons are, in order: **New Path**, **Raise Paths**, **Lower Paths**, **Duplicate Paths**, **Paths to Selection**, **Selection to Path**, **Paint along the paths**, and **Delete Paths**. The right-click menu adds **Edit Path Attributes** (rename), **Merge Visible Paths**, **Add/Subtract/Intersect Paths with Selection**, **Fill Paths**, **Stroke Paths…**, **Copy Paths**, **Paste Path**, **Export Paths…**, and **Import Path…**.

## Path to/from selection

Use **Selection to Path** to build a new path from the current selection (also **Select > To Path**). Going the other way, **Paths to Selection** turns the active path into a selection; the same conversion is the Select menu's **Selection From Paths**.

```text
Selection to Path  : pixel selection → editable vector path
Paths to Selection : vector path → pixel selection
```

## Stroking a path

**Stroke Paths…** (also the Paths dialog button **Paint along the paths**, and **Edit > Stroke Paths…**) opens the **Choose Stroke Style** dialog and is active only when the image has a path. Its Line section offers **Foreground color**, **Background color**, **Pattern**, **Antialiasing**, **Line width** (default unit pixels), **Cap style** (Butt, Round, Square), **Join style** (Miter, Round, Bevel), **Miter limit**, and **Dash pattern**; alternatively choose **Paint tool** with **Emulate brush dynamics**.

```text
Edit > Stroke Paths…  → Choose Stroke Style → Line, Line width = 3 (pixels), Cap style = Round
```

## SVG import/export

Paths interchange as SVG. **Export Paths…** saves a path to a file in SVG format; **Import Path…** creates a new path from an SVG file. Both live in the Paths dialog's context menu.

## Do / Don't

- **Do** create with **Paths Edit Mode** set to **Design**, then refine handles before converting.
- **Do** convert with **Paths to Selection** / **Selection to Path** instead of redrawing by hand.
- **Don't** expect **Stroke Paths…** to do anything without an existing path — the command is disabled otherwise.
- **Don't** flatten a path into a selection prematurely; keep the vector path for non-destructive re-editing and SVG export.

## Related

[selections](selections.md) · [masks and channels](masks-and-channels.md) · [tools overview](tools-overview.md) · [pdb recipes selections paths](pdb-recipes-selections-paths.md)
