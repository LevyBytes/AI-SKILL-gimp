# Interface and Workflow

GIMP 3.2 arranges its tools, panels, and image canvas around a configurable workspace driven by a single top menu bar. This file maps that workspace so an agent can locate any command, panel, or window control.

**When this applies:** Read this when you need to describe GIMP's windows, panels, menus, zoom/navigation, undo, or how to set an image's color **Mode** or **Encoding**.

## Single-window vs multi-window

GIMP runs either as one unified workspace or as separate floating panels. Toggle between them with **Windows > Single-Window Mode**; the choice persists across restarts. In single-window mode the left and right panels are fixed in place (resize by dragging their borders), and opening several images adds a bar above the canvas with one tab per image.

```text
Windows > Single-Window Mode    (toggle the unified layout on or off)
```

## The image window

Below the Title Bar sits the Main Menu; the small arrow-head Menu Button at the upper left reopens it as a column (or press **Shift+F10**). A Ruler runs above and to the left, defaulting to pixels, and dragging from a ruler creates a guide. The lower left holds the Quick Mask toggle (outlined red when active) and the Pointer Coordinates readout; the bottom Status Area shows the filename and the memory the image uses. The Navigation Control sits at the lower right.

## Docks, dialogs, and tabs

A dialog is a movable window of options or a dedicated task panel; a dock is a container holding persistent dialogs. Three docks ship by default, grouping panels such as Tool Options, Undo History, Layers, Channels, and Paths into tabbed sets. Add panels through **Windows > Dockable Dialogs**, manage tabs from each dock's Tab Menu (Add Tab, Detach Tab, View as List or Grid), and press **Tab** over the canvas to hide or show all docks.

```text
Windows > Dockable Dialogs    (pick a panel to add as a tab)
```

## Zoom, navigation, and undo

Pan with **Shift**+arrow keys, the scroll wheel (**Shift**+scroll for horizontal), middle-button drag, or **Spacebar**+mouse. **Ctrl+J** fits the window to the image; **Ctrl+Shift+J** fits the image to the window. The Undo History panel shows thumbnails of every prior state; **Ctrl+Z** steps back one operation, and clicking a thumbnail jumps directly to that state.

```text
Edit > Undo History    (no default shortcut; click any thumbnail to restore that state)
```

## Mode and Encoding

Color mode lives under **Image > Mode** with three choices: RGB, Grayscale, and Indexed (8-bit grayscale spans 0 black to 255 white; indexed supports at most 256 palette entries). Bit depth and gamma are separate, under **Image > Encoding**: integer precision (8-bit integer, 16-bit integer, 32-bit integer) or floating point (16-bit floating point, 32-bit floating point), each paired with a Linear light or Non-linear channel encoding. Floating point allows values beyond the 0.0 to 1.0 range for HDR work, while integer storage clips to its numeric channel range, not a monitor gamut.

```text
Image > Mode > RGB        Image > Encoding > 32-bit floating point > Linear light
```

## Do / Don't

- **Do** call the bit-depth menu **Image > Encoding** in 3.2, not "Precision".
- **Do** convert indexed images to RGB before heavy editing, since many tools and filters work poorly on indexed color.
- **Don't** confuse Mode (color model) with Encoding (bit depth and gamma); they are separate submenus.
- **Don't** assume a keyboard shortcut for Undo History; it has none by default.

## Related

[tools overview](tools-overview.md) · [layers and modes](layers-and-modes.md) · [colors and adjustments](colors-and-adjustments.md) · [file formats and export](file-formats-and-export.md)
