# File Formats and Export

GIMP 3.2 separates saving its own project format from exporting to interchange formats, a distinction that trips up newcomers. This file explains how images come in, how they go out, and the per-format options worth knowing.

**When this applies:** Read this for opening, importing, saving, exporting, overwriting, or choosing PNG/JPEG export options.

## Opening and importing

Use **File > Open…** (**Ctrl+O**) to load a file. Opening a non-XCF file such as a PNG imports it into GIMP's own XCF representation as a new project rather than editing the original in place. **File > Open as Layers…** (**Ctrl+Alt+O**) instead drops the chosen file's layers on top of the current image's stack. Dragging a file onto the Toolbox opens it; dragging onto an open image adds it as new layers. **File > Open Location…** loads from a URI, and **File > Open Recent** lists recent files.

```text
File > Open as Layers…    (Ctrl+Alt+O — adds the file as the top layers)
```

## Saving the native format

**File > Save** and **File > Save As…** (**Shift+Ctrl+S**) write only GIMP's native XCF format, the one format that preserves all image data including layers and transparency. For anything else, you export.

```text
File > Save As…    (Shift+Ctrl+S — writes .xcf only)
```

## Exporting to other formats

**File > Export As…** (**Shift+Ctrl+E**) chooses a destination and format. Before a destination is established, **Export** can open that dialog too. After exporting, **Export to filename** repeats the export to the chosen destination. For an imported image, **Overwrite filename.extension** writes back to its source format. Exporting leaves the working image intact, but the exported file may lose layers, transparency, precision or metadata depending on its format and settings; save an XCF to preserve editable work.

```text
File > Export As…    (Shift+Ctrl+E — opens the "Export Image" dialog)
```

## PNG export options

The PNG Export dialog (extension .png) exposes Pixel format, Compression level (default 9; compression is not lossy), Interlacing, Save background color, Save resolution, Save creation time, Save comment, and metadata toggles (Save Exif data, Save IPTC data, Save XMP data, Save color profile, Save thumbnail).

## JPEG export options

The JPEG Export dialog (extensions .jpg, .JPG, .jpeg) centers on Quality (0 to 100, default 85), plus Smoothing, Progressive, Optimize, and subsampling. Subsampling choices are "4:4:4 (best quality)", "4:2:2 (chroma halved horizontally)", "4:4:0 (chroma halved vertically)", and "4:2:0 (chroma quartered)"; the DCT method offers Fast Integer, Integer (default), and Floating-Point.

```text
File > Export As…  →  name the file image.jpg  →  set Quality to 85
```

TODO: TIFF, WebP, and PDF export option pages were not confirmed in the pages fetched; the in-domain index linked only JPEG, GIF, and PNG. Verify other formats' options before relying on them.

## Do / Don't

- **Do** use **File > Save** for .xcf and **File > Export As…** for PNG, JPEG, and other delivery formats.
- **Do** reach for **File > Overwrite** to re-export an imported file in its original format quickly.
- **Don't** expect **File > Save** to produce a PNG or JPEG; it writes only XCF.
- **Don't** assume an export changed your project; exporting leaves the working image untouched.

## Related

[interface and workflow](interface-and-workflow.md) · [layers and modes](layers-and-modes.md) · [pdb recipes io batch](pdb-recipes-io-batch.md) · [scripting overview](scripting-overview.md)
