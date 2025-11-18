#!/usr/bin/env python3
import re
import json

# Read the FrankenUI CSS file
with open('vite/node_modules/franken-ui/dist/css/franken-ui.css', 'r') as f:
    css_content = f.read()

# Define the themes we're looking for
themes = ['zinc', 'slate', 'gray', 'neutral', 'blue', 'red', 'green', 'orange', 
          'yellow', 'violet', 'purple', 'rose', 'amber', 'teal', 'stone']

frankenui_themes = {}

# Extract theme values for each theme
for theme in themes:
    frankenui_themes[theme] = {'light': {}, 'dark': {}}
    
    # Extract light mode values
    light_pattern = rf'\.uk-theme-{theme}\s*{{([^}}]+)}}'
    light_match = re.search(light_pattern, css_content, re.DOTALL)
    if light_match:
        variables = light_match.group(1)
        for line in variables.split('\n'):
            if '--' in line:
                # Parse CSS variable
                match = re.match(r'\s*(--[\w-]+):\s*([^;]+);', line)
                if match:
                    var_name = match.group(1)
                    var_value = match.group(2).strip()
                    frankenui_themes[theme]['light'][var_name] = var_value
    
    # Extract dark mode values
    dark_pattern = rf'\.dark\.uk-theme-{theme}\s*{{([^}}]+)}}'
    dark_match = re.search(dark_pattern, css_content, re.DOTALL)
    if dark_match:
        variables = dark_match.group(1)
        for line in variables.split('\n'):
            if '--' in line:
                # Parse CSS variable
                match = re.match(r'\s*(--[\w-]+):\s*([^;]+);', line)
                if match:
                    var_name = match.group(1)
                    var_value = match.group(2).strip()
                    frankenui_themes[theme]['dark'][var_name] = var_value

# Also extract the default theme (no class)
frankenui_themes['default'] = {'light': {}, 'dark': {}}

# Extract default light values from :root
root_pattern = r':root\s*{([^}]+)}'
root_match = re.search(root_pattern, css_content, re.DOTALL)
if root_match:
    variables = root_match.group(1)
    for line in variables.split('\n'):
        if '--' in line and ('--background' in line or '--foreground' in line or '--primary' in line or 
                           '--secondary' in line or '--muted' in line or '--accent' in line or 
                           '--destructive' in line or '--border' in line or '--input' in line or '--ring' in line):
            match = re.match(r'\s*(--[\w-]+):\s*([^;]+);', line)
            if match:
                var_name = match.group(1)
                var_value = match.group(2).strip()
                frankenui_themes['default']['light'][var_name] = var_value

# Extract default dark values
dark_pattern = r'\.dark\s*{([^}]+)}'
dark_match = re.search(dark_pattern, css_content, re.DOTALL)
if dark_match:
    variables = dark_match.group(1)
    for line in variables.split('\n'):
        if '--' in line and ('--background' in line or '--foreground' in line or '--primary' in line or 
                           '--secondary' in line or '--muted' in line or '--accent' in line or 
                           '--destructive' in line or '--border' in line or '--input' in line or '--ring' in line):
            match = re.match(r'\s*(--[\w-]+):\s*([^;]+);', line)
            if match:
                var_name = match.group(1)
                var_value = match.group(2).strip()
                frankenui_themes['default']['dark'][var_name] = var_value

# Save to JSON
with open('frankenui_themes.json', 'w') as f:
    json.dump(frankenui_themes, f, indent=2)

print(f"Extracted {len(frankenui_themes)} FrankenUI themes")
for theme in frankenui_themes:
    light_vars = len(frankenui_themes[theme]['light'])
    dark_vars = len(frankenui_themes[theme]['dark'])
    print(f"  {theme}: {light_vars} light variables, {dark_vars} dark variables")