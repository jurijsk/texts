#!/usr/bin/env python3
"""
Script to extract embedded resources from the Engelbart HTML file
"""
import re
import base64
import os
from pathlib import Path

def extract_embedded_resources(html_file):
    """Extract embedded CSS, images, and other resources from HTML file"""
    
    # Read the HTML file
    with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Create directories
    assets_dir = Path('assets')
    css_dir = assets_dir / 'css'
    images_dir = assets_dir / 'images'
    js_dir = assets_dir / 'js'
    
    for dir_path in [assets_dir, css_dir, images_dir, js_dir]:
        dir_path.mkdir(exist_ok=True)
    
    # Extract CSS styles
    css_blocks = []
    style_pattern = r'<style[^>]*>(.*?)</style>'
    style_matches = re.findall(style_pattern, content, re.DOTALL | re.IGNORECASE)
    
    for i, css_content in enumerate(style_matches, 1):
        css_file = css_dir / f'style_{i:02d}.css'
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(css_content.strip())
        css_blocks.append((f'<style>{css_content}</style>', f'<link rel="stylesheet" href="assets/css/style_{i:02d}.css">'))
        print(f"Extracted CSS block {i} to {css_file}")
    
    # Extract base64 images
    image_count = 1
    image_replacements = []
    
    # Pattern for data URLs
    data_url_pattern = r'data:image/([^;]+);base64,([A-Za-z0-9+/=]+)'
    data_matches = re.finditer(data_url_pattern, content)
    
    for match in data_matches:
        image_type = match.group(1)
        base64_data = match.group(2)
        
        # Determine file extension
        if image_type == 'x-icon':
            ext = 'ico'
        else:
            ext = image_type
        
        # Generate filename
        image_filename = f'image_{image_count:02d}.{ext}'
        image_path = images_dir / image_filename
        
        try:
            # Decode and save image
            image_data = base64.b64decode(base64_data)
            with open(image_path, 'wb') as f:
                f.write(image_data)
            
            # Store replacement info
            original_data_url = match.group(0)
            new_url = f'assets/images/{image_filename}'
            image_replacements.append((f'data:image/{image_type};base64,{base64_data}', new_url))
            
            print(f"Extracted image {image_count} ({image_type}) to {image_path}")
            image_count += 1
            
        except Exception as e:
            print(f"Error processing image {image_count}: {e}")
            continue
    
    # Create modified HTML
    modified_content = content
    
    # Replace CSS blocks
    for original, replacement in css_blocks:
        modified_content = modified_content.replace(original, replacement)
    
    # Replace image data URLs
    for original_url, new_url in image_replacements:
        modified_content = modified_content.replace(original_url, new_url)
    
    # Write modified HTML
    output_file = 'index.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(modified_content)
    
    print(f"\nModified HTML saved as {output_file}")
    print(f"Extracted {len(css_blocks)} CSS blocks and {image_count-1} images")
    
    return output_file

if __name__ == '__main__':
    import glob
    html_files = glob.glob('*.html')
    html_file = None
    for f in html_files:
        if 'Augmenting' in f and f != 'temp.html':
            html_file = f
            break
    
    if html_file:
        print(f"Processing file: {html_file}")
        extract_embedded_resources(html_file)
    else:
        print("Could not find the Engelbart HTML file")
