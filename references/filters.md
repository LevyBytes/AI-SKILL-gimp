# Filters

How the **Filters** menu is organized and how to reapply the last filter. A filter takes an input layer or image, applies an algorithm, and returns it in a modified form.

**When this applies:** Read this when an agent must locate a filter category, build a Filters menu path, or reapply or re-open the most recent filter.

## The Filters menu layout

The **Filters** menu opens with **Filters > Repeat Last** and **Filters > Re-Show Last**, followed by **Filters > Reset All Filters**, then the category submenus. The **Development** submenu contains **Script-Fu** and **Python-Fu** console entries when installed (see [scripting overview](scripting-overview.md)).

## Filter categories

The filter categories, as the manual titles them, are **Blur Filters**, **Enhance Filters**, **Distort Filters**, **Light and Shadow Filters**, **Noise Filters**, **Edge-Detect Filters**, **Generic Filters**, **Combine Filters**, **Artistic Filters**, **Decor Filters**, **Map Filters**, **Rendering Filters**, **Web Filters**, and **Animation Filters**.

These are documentation chapter titles, not a literal list of submenu labels. Use the actual installed menu label when giving a command path.

```text
Filters > Blur > …
Filters > Light and Shadow > …
Filters > Edge-Detect > …
```

## Repeat Last and Re-Show Last

**Filters > Repeat Last** (**Ctrl+F**) performs the most recently executed filter again using the same settings as the previous run. **Filters > Re-Show Last** (**Ctrl+Shift+F**) instead re-opens the dialog of the most recently executed filter so the settings can be changed before running.

```text
Apply Gaussian Blur once → Ctrl+F repeats it with identical settings
                         → Ctrl+Shift+F re-opens its dialog to adjust first
```

## Do / Don't

- **Do** use **Ctrl+F** to reapply the exact last filter, and **Ctrl+Shift+F** to reapply it with changes.
- **Do** reach the scripting consoles through the **Filters > Development** submenu (see [scripting overview](scripting-overview.md)).
- **Don't** infer a literal menu label from a documentation chapter title.
- **Don't** assume a filter's specific dialog options from this map; open the filter to read them.

## Related

[colors and adjustments](colors-and-adjustments.md) · [scripting overview](scripting-overview.md) · [pdb recipes color filters](pdb-recipes-color-filters.md) · [interface and workflow](interface-and-workflow.md)
