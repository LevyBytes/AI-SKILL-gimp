# Colors and Adjustments

How GIMP exposes color adjustment operations through the **Colors** menu, plus the color-management essentials that govern how pixel values are interpreted and converted.

**When this applies:** Read this when an agent must name a color operation, build a menu path to it, or reason about ICC profiles, working space, soft-proofing, or the assign-versus-convert distinction.

## Foreground and background color

The toolbox carries two active colors, the foreground and the background. Clicking either swatch opens a color selection dialog where a color can be set by HSV, RGB, or hexadecimal entry, or sampled from the canvas. These colors feed painting, filling, and gradient operations.

```text
Click the foreground swatch in the toolbox → color selection dialog → set by RGB/HSV/Hex → OK
```

## The Colors menu adjustments

Top-level entries include **Colors > Color Balance**, **Colors > Color Temperature**, **Colors > Hue Chroma**, **Colors > Hue-Saturation**, **Colors > Saturation**, **Colors > Exposure**, **Colors > Shadows-Highlights**, **Colors > Brightness-Contrast**, **Colors > Levels**, **Colors > Curves**, **Colors > Invert**, **Colors > Linear Invert**, **Colors > Value Invert**, **Colors > Threshold**, **Colors > Colorize**, **Colors > Posterize**, and **Colors > Color to Alpha…**.

Preserve the exact spelling: it is **Hue Chroma** (a space, no hyphen) but **Hue-Saturation** (hyphenated). **Invert**, **Linear Invert**, and **Value Invert** are three distinct operations.

```text
Colors > Curves…        # tonal curve per channel
Colors > Levels         # black/white/gamma input-output mapping
Colors > Hue-Saturation # shift hue, lightness, saturation
```

## Colors submenus

Related operations live in submenus: **Auto** (Equalize, White Balance, Stretch Contrast, Stretch Contrast HSV, Color Enhance); **Components** (Channel Mixer, Extract Component, Mono Mixer, Compose, Decompose, Recompose); **Desaturate** (Color to Gray, Desaturate, Sepia); **Map** (Rearrange Colormap, Set Colormap, Alien Map, Color Exchange, Rotate Colors, Gradient Map, Palette Map, Sample Colorize); **Tone Mapping**; and **Info** (Histogram, Export Histogram, Border Average, Smooth Palette).

## Color management: assign vs convert

Two operations are easy to confuse and must never be swapped.

- **Image > Color Management > Assign Color Profile** assigns a new ICC profile to the image. It changes the profile the existing pixel values are interpreted through; it does not run a colorimetric recalculation, so the displayed colors can change.
- **Image > Color Management > Convert to Color Profile…** converts the image from its currently assigned ICC profile to another, recalculating pixel data through a chosen rendering intent to preserve appearance as closely as the destination gamut and rendering intent allow.

Convert offers a **Rendering Intent** of **Perceptual**, **Relative colorimetric**, **Saturation**, or **Absolute colorimetric**, plus **Black Point Compensation**. The working space is sRGB by default.

```text
Assign  = retag / reinterpret (no recalculation; look may shift)
Convert = recompute pixels source→destination via rendering intent (appearance may change with gamut/intent)
```

The same submenu exposes **Soft-Proof Profile**, **Soft-Proofing Rendering Intent**, and **Black Point Compensation** to simulate an output device on screen.

## Do / Don't

- **Do** use **Convert to Color Profile…** when changing the pixel encoding for a new profile; inspect gamut and rendering-intent effects.
- **Do** use **Assign Color Profile** only to set or correct which profile an untagged or mistagged image is read through.
- **Don't** write "Hue-Chroma" or "Convert Color Profile" — the labels are **Hue Chroma** and **Convert to Color Profile**.
- **Don't** swap assign and convert: assign reinterprets, convert recalculates.

## Related

[filters](filters.md) · [interface and workflow](interface-and-workflow.md) · [tools overview](tools-overview.md) · [pdb recipes color filters](pdb-recipes-color-filters.md)
