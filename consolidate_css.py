#!/usr/bin/env python3
"""
Script to consolidate CSS references in the HTML file
"""
import re

def consolidate_css_references():
    # Read the index.html file
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace multiple CSS links with a single one
    css_pattern = r'<link rel="stylesheet" href="assets/css/style_\d+\.css">'
    content = re.sub(css_pattern, '', content)

    # Add single CSS link in the head
    head_end = content.find('</head>')
    if head_end != -1:
        css_link = '    <link rel="stylesheet" href="assets/css/styles.css">\n'
        content = content[:head_end] + css_link + content[head_end:]

    # Write updated file
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print('Updated index.html with consolidated CSS reference')

if __name__ == '__main__':
    consolidate_css_references()
