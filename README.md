# Engelbart Project

A Node.js project setup with http-server for serving the "Augmenting Human Intellect" document with extracted static assets.

## Available Scripts

- `npm start` - Start http-server with default settings (port 8080)
- `npm run serve` - Start http-server on port 3000 and automatically open browser
- `npm run dev` - Start http-server on port 8080, open browser, and disable caching for development
- `npm run serve-doc` - Start http-server and open the Augmenting Human Intellect document directly

## Usage

To start the server:
```bash
npm start
```

To start the server and open browser automatically:
```bash
npm run serve
```

To open the main document directly:
```bash
npm run serve-doc
```

For development with no caching:
```bash
npm run dev
```

## Files

- `Augmenting-Human-Intellect.html` - The main document with external asset references
- `assets/` - Extracted CSS, images, and other resources
- `utils/` - Python scripts for future transformations

The server will serve files from the current directory and make your HTML files accessible via the browser.
