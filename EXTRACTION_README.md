# Engelbart Document - Resource Extraction

## Overview
This project contains the "Augmenting Human Intellect: A Conceptual Framework" document by Doug Engelbart (1962), with all embedded resources extracted into organized folders.

## Project Structure

```
engelbart/
├── index.html                    # Main HTML document (cleaned, references external assets)
├── assets/
│   ├── css/                     # Stylesheets
│   │   ├── styles.css          # Main consolidated stylesheet
│   │   ├── fonts.css           # Font face declarations
│   │   ├── root-variables.css  # CSS custom properties
│   │   ├── main-styles.css     # Core document styles  
│   │   └── style_*.css         # Individual style blocks
│   ├── images/                 # All extracted images
│   │   ├── image_01.gif        # Background patterns
│   │   ├── image_*.jpeg        # Various document images
│   │   ├── image_*.png         # Icons and graphics
│   │   └── image_06.ico        # Favicon
│   ├── fonts/                  # Extracted font files
│   │   ├── Inter_VF_*.woff2    # Inter Variable Font (normal & italic)
│   │   ├── Source_Serif_VF_*.woff2 # Source Serif Variable Font
│   │   ├── Roboto_Mono_VF_*.ttf    # Roboto Mono Variable Font
│   │   └── Public_Sans_VF_*.ttf    # Public Sans Variable Font
│   └── js/                     # JavaScript files (if any)
├── package.json                # Node.js project configuration
├── README.md                   # Project documentation
└── utils/                      # Transformation scripts
    ├── extract_embedded.py    # Extract CSS and images
    ├── extract_fonts.py       # Extract embedded fonts
    └── consolidate_css.py     # Consolidate CSS references
```

## Extracted Resources

### CSS Files (9 blocks extracted)
- **Root Variables**: CSS custom properties and theme colors
- **Main Styles**: Core document layout and typography
- **Navigation Styles**: Top navigation and menu styling
- **Content Styles**: Article content formatting
- **Responsive Styles**: Media queries and responsive design

### Images (27 files extracted)
- **1 GIF**: Small background pattern
- **11 JPEG**: Various document images and backgrounds
- **14 PNG**: Icons, graphics, and interface elements  
- **1 ICO**: Website favicon

### Fonts (8 files extracted)
- **4 WOFF2**: Modern web fonts (Inter VF, Source Serif VF)
- **4 TTF**: TrueType fonts (Roboto Mono VF, Public Sans VF)
- All fonts are variable fonts supporting multiple weights and styles

## Development Commands

- `npm start` - Start HTTP server on default port (8080)
- `npm run serve` - Start server on port 3000 and open browser
- `npm run dev` - Start development server with no caching

## Benefits of Resource Extraction

1. **Better Performance**: External files can be cached separately
2. **Easier Maintenance**: CSS and images can be modified independently
3. **Development Friendly**: Separate files are easier to work with
4. **Optimization Ready**: Images and CSS can be optimized/minified
5. **Version Control**: Individual resources can be tracked separately

## Technical Notes

- All `data:` URLs have been replaced with proper file references
- CSS has been organized into logical components
- Original document structure and functionality preserved
- All external links remain unchanged
