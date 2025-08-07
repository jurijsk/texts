# Transformation Utilities

This folder contains Python scripts used for transforming the original HTML document.

## Scripts

### extract_embedded.py
Extracts embedded resources (CSS, images) from HTML files and creates external files.

**Features:**
- Extracts inline CSS `<style>` blocks to separate `.css` files
- Converts base64 data URLs to image files
- Updates HTML references to point to external files
- Maintains original document structure

**Usage:**
```bash
python utils/extract_embedded.py
```

### extract_fonts.py
Extracts embedded font files from HTML documents and creates external font files.

**Features:**
- Extracts fonts from `@font-face` declarations with data URLs
- Supports WOFF2 and TTF font formats
- Generates descriptive filenames based on font-family, weight, and style
- Creates a consolidated `fonts.css` file with all font-face declarations
- Updates HTML references to point to external font files

**Usage:**
```bash
python utils/extract_fonts.py
```

### consolidate_css.py
Updates HTML files to use consolidated CSS references instead of multiple individual CSS files.

**Features:**
- Removes multiple CSS link references
- Adds single consolidated CSS file reference
- Preserves document structure

**Usage:**
```bash
python utils/consolidate_css.py
```

## Notes

These scripts were used to transform the original "Augmenting Human Intellect" document from a single HTML file with embedded resources to a properly structured web project with external assets.

The transformation process:
1. Extracted 9 CSS blocks and 27 images from the original HTML
2. Extracted 8 embedded fonts (4 WOFF2, 4 TTF) to separate files
3. Created organized folder structure (`assets/css/`, `assets/images/`, `assets/fonts/`)
4. Updated all references in the HTML to point to external files
5. Generated the final `Augmenting-Human-Intellect.html` file

This approach provides better maintainability, performance, and development experience.
