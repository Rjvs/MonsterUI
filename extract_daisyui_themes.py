#!/usr/bin/env python3
import re
import json
import os

# DaisyUI themes from the configuration
daisy_themes = [
    "light", "dark", "cupcake", "bumblebee", "emerald", "corporate", 
    "synthwave", "retro", "cyberpunk", "valentine", "halloween", "garden", 
    "forest", "aqua", "lofi", "pastel", "fantasy", "wireframe", "black", 
    "luxury", "dracula", "cmyk", "autumn", "business", "acid", "lemonade", 
    "night", "coffee", "winter", "dim", "nord", "sunset"
]

daisyui_themes = {}

# Extract theme values for each theme
for theme in daisy_themes:
    theme_file = f'vite/node_modules/daisyui/theme/{theme}.css'
    
    if os.path.exists(theme_file):
        with open(theme_file, 'r') as f:
            css_content = f.read()
            
        daisyui_themes[theme] = {}
        
        # Extract variables from the theme file
        # Look for CSS custom properties
        for line in css_content.split('\n'):
            if '--' in line:
                match = re.match(r'\s*(--[\w-]+):\s*([^;]+);', line)
                if match:
                    var_name = match.group(1)
                    var_value = match.group(2).strip()
                    daisyui_themes[theme][var_name] = var_value
        
        # Also extract color-scheme
        if 'color-scheme:' in css_content:
            scheme_match = re.search(r'color-scheme:\s*(\w+);', css_content)
            if scheme_match:
                daisyui_themes[theme]['color-scheme'] = scheme_match.group(1)

# Save to JSON
with open('daisyui_themes.json', 'w') as f:
    json.dump(daisyui_themes, f, indent=2)

print(f"Extracted {len(daisyui_themes)} DaisyUI themes")
for theme in daisyui_themes:
    var_count = len(daisyui_themes[theme])
    print(f"  {theme}: {var_count} variables")