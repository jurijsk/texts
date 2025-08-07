#!/usr/bin/env python3
"""
Script to extract embedded fonts from the HTML file
"""
import re
import base64
import os
from pathlib import Path

def extract_embedded_fonts(html_file):
    """Extract embedded fonts from HTML file"""
    
    # Read the HTML file
    with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Create fonts directory
    fonts_dir = Path('assets/fonts')
    fonts_dir.mkdir(exist_ok=True)
    
    # Find all @font-face declarations
    font_face_pattern = r'@font-face\s*{([^}]+)}'
    font_matches = re.finditer(font_face_pattern, content, re.DOTALL | re.IGNORECASE)
    
    font_replacements = []
    font_count = 1
    
    for match in font_matches:
        font_face_content = match.group(1)
        
        # Extract font-family name
        family_match = re.search(r'font-family:\s*["\']?([^;"\']+)["\']?', font_face_content)
        font_family = family_match.group(1).strip() if family_match else f"font_{font_count}"
        
        # Extract font-weight if present
        weight_match = re.search(r'font-weight:\s*([^;]+)', font_face_content)
        font_weight = weight_match.group(1).strip() if weight_match else "400"
        
        # Extract font-style if present
        style_match = re.search(r'font-style:\s*([^;]+)', font_face_content)
        font_style = style_match.group(1).strip() if style_match else "normal"
        
        # Find data URL within this font-face
        data_url_match = re.search(r'url\(data:font/([^;]+);base64,([A-Za-z0-9+/=]+)\)', font_face_content)
        
        if data_url_match:
            font_format = data_url_match.group(1)  # woff2, ttf, etc.
            base64_data = data_url_match.group(2)
            
            # Create filename
            safe_family = re.sub(r'[^\w\-_]', '', font_family.replace(' ', '_'))
            safe_weight = re.sub(r'[^\w\-_]', '', str(font_weight))
            safe_style = re.sub(r'[^\w\-_]', '', font_style)
            
            if safe_style == "normal":
                font_filename = f"{safe_family}_{safe_weight}.{font_format}"
            else:
                font_filename = f"{safe_family}_{safe_weight}_{safe_style}.{font_format}"
            
            font_path = fonts_dir / font_filename
            
            try:
                # Decode and save font
                font_data = base64.b64decode(base64_data)
                with open(font_path, 'wb') as f:
                    f.write(font_data)
                
                # Store replacement info
                original_url = data_url_match.group(0)
                new_url = f'url(assets/fonts/{font_filename})'
                font_replacements.append((original_url, new_url))
                
                print(f"Extracted font {font_count}: {font_filename} ({font_format}) - {font_family} {font_weight} {font_style}")
                font_count += 1
                
            except Exception as e:
                print(f"Error processing font {font_count}: {e}")
                continue
    
    # Replace font URLs in content
    modified_content = content
    for original_url, new_url in font_replacements:
        modified_content = modified_content.replace(original_url, new_url)
    
    # Write modified HTML
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(modified_content)
    
    print(f"\nExtracted {font_count-1} fonts and updated {html_file}")
    
    # Create a fonts.css file with all font-face declarations
    create_fonts_css(modified_content)
    
    return font_count - 1

def create_fonts_css(content):
    """Extract all @font-face declarations to a separate CSS file"""
    font_face_pattern = r'@font-face\s*{[^}]+}'
    font_faces = re.findall(font_face_pattern, content, re.DOTALL | re.IGNORECASE)
    
    if font_faces:
        fonts_css_path = Path('assets/css/fonts.css')
        with open(fonts_css_path, 'w', encoding='utf-8') as f:
            f.write("/* Font Face Declarations */\n\n")
            for font_face in font_faces:
                f.write(font_face + "\n\n")
        
        print(f"Created fonts.css with {len(font_faces)} font-face declarations")

if __name__ == '__main__':
    html_file = 'Augmenting-Human-Intellect.html'
    extract_embedded_fonts(html_file)
