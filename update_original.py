#!/usr/bin/env python3
"""
Script to update the original Engelbart HTML file to use external assets
"""
import re
import glob

def update_original_html():
    """Update the original HTML file to reference external assets"""
    
    # Find the original HTML file
    html_files = glob.glob('*.html')
    original_file = None
    for f in html_files:
        if 'Augmenting' in f:
            original_file = f
            break
    
    if not original_file:
        print("Could not find the original Engelbart HTML file")
        return
    
    print(f"Updating original file: {original_file}")
    
    # Read the original file
    with open(original_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Create a backup
    backup_file = 'engelbart-original-backup.html'
    with open(backup_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Backup created: {backup_file}")
    
    # Replace inline styles with external CSS links
    # Remove all <style> blocks and replace with external CSS links
    
    # First, let's add the external CSS link in the head section
    head_pattern = r'(<head[^>]*>)'
    css_links = '''<link rel="stylesheet" href="assets/css/root-variables.css">
    <link rel="stylesheet" href="assets/css/style_02.css">
    <link rel="stylesheet" href="assets/css/main-styles.css">
    <link rel="stylesheet" href="assets/css/style_04.css">
    <link rel="stylesheet" href="assets/css/style_05.css">
    <link rel="stylesheet" href="assets/css/style_06.css">
    <link rel="stylesheet" href="assets/css/style_07.css">
    <link rel="stylesheet" href="assets/css/style_08.css">
    <link rel="stylesheet" href="assets/css/style_09.css">'''
    
    content = re.sub(head_pattern, r'\1\n' + css_links + '\n', content, flags=re.IGNORECASE)
    
    # Remove inline <style> blocks
    style_pattern = r'<style[^>]*>.*?</style>'
    content = re.sub(style_pattern, '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Replace data URLs with external image references
    image_replacements = [
        # Based on the extraction, create mappings
        (r'data:image/gif;base64,R0lGODlhCAAJANUqAEJ8rEB9qj58r0F7rWWWvm\+Zv0N7rOLq9UB8rmmVvGWWwWmWwMjc57HO4EiDrUSBrWqXuHKixt/s9ZW30r3T6FiLuEJ6qUF8pkN7qmaVvz2AqkJ8qtjk8n6lxLPJ4WaTvEB8sKa\+1j99rmqVv0V9rLPK2k2Eqz97rYqsz9Di7v///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAACoALAAAAAAIAAkAAAY0wEhIRSyOBh/KoQgBGDadFDETOAECjokqIbCQMCKTZ6EBIB4ojkpxARUYEiKh0igSS/ZiEAA7', 'assets/images/image_01.gif'),
    ]
    
    # Replace all data: URLs with external references
    data_url_pattern = r'data:image/([^;]+);base64,[A-Za-z0-9+/=]+'
    
    image_counter = 1
    def replace_data_url(match):
        nonlocal image_counter
        image_type = match.group(1)
        if image_type == 'x-icon':
            ext = 'ico'
        else:
            ext = image_type
        
        replacement = f'assets/images/image_{image_counter:02d}.{ext}'
        image_counter += 1
        return replacement
    
    content = re.sub(data_url_pattern, replace_data_url, content)
    
    # Also fix the root CSS variable reference
    content = re.sub(r'--sf-img-1: url\("data:image/gif;base64,[^"]+"\)', '--sf-img-1: url("assets/images/image_01.gif")', content)
    
    # Write the updated file back
    with open(original_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Successfully updated {original_file}")
    print("The original file now references external CSS and image assets")
    print("All embedded resources have been moved to the assets/ folder")

if __name__ == '__main__':
    update_original_html()
