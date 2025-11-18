#!/usr/bin/env python3
"""Test script for Tailwind CSS extraction"""

from itertools import product
import httpx
from pathlib import Path
import subprocess
import re
import tempfile
import json

# Copy all the functions from the notebook
TAILWIND_CDN = "https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"

SPACING = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 72, 80, 96]
TEXT_SIZES = ["xs", "sm", "base", "lg", "xl", "2xl", "3xl", "4xl", "5xl", "6xl", "7xl", "8xl", "9xl"]
FONT_WEIGHTS = ["thin", "extralight", "light", "normal", "medium", "semibold", "bold", "extrabold", "black"]
SHADES = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950]
COLORS = ["slate", "gray", "zinc", "neutral", "stone", "red", "orange", "amber", "yellow", "lime", "green", "emerald", "teal", "cyan", "sky", "blue", "indigo", "violet", "purple", "fuchsia", "pink", "rose"]
OPACITY = [0, 5, 10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 95, 100]
ROUNDED = ["none", "sm", "", "md", "lg", "xl", "2xl", "3xl", "full"]
BORDER_WIDTH = [0, 2, 4, 8]

def download_tailwind_bundle():
    """Download the Tailwind browser bundle from CDN"""
    print(f"Downloading {TAILWIND_CDN}...")
    response = httpx.get(TAILWIND_CDN, follow_redirects=True)
    response.raise_for_status()
    return response.text

def generate_test_classes():
    """Generate a comprehensive set of Tailwind classes to test"""
    classes = set()

    # Layout & Display
    classes.update(["block", "inline-block", "inline", "flex", "inline-flex", "grid", "inline-grid", "hidden"])
    classes.update(["static", "fixed", "absolute", "relative", "sticky"])

    # Flexbox & Grid
    classes.update(["flex-row", "flex-col", "flex-wrap", "flex-nowrap"])
    classes.update(["justify-start", "justify-end", "justify-center", "justify-between", "justify-around", "justify-evenly"])
    classes.update(["items-start", "items-end", "items-center", "items-baseline", "items-stretch"])
    classes.update(["grid-cols-1", "grid-cols-2", "grid-cols-3", "grid-cols-4", "grid-cols-6", "grid-cols-12"])

    # Spacing (padding, margin, gap, space)
    for n in SPACING:
        n_str = str(n).replace(".", "_")
        classes.update([f"p-{n_str}", f"px-{n_str}", f"py-{n_str}", f"pt-{n_str}", f"pr-{n_str}", f"pb-{n_str}", f"pl-{n_str}"])
        classes.update([f"m-{n_str}", f"mx-{n_str}", f"my-{n_str}", f"mt-{n_str}", f"mr-{n_str}", f"mb-{n_str}", f"ml-{n_str}"])
        classes.update([f"gap-{n_str}", f"gap-x-{n_str}", f"gap-y-{n_str}"])
        classes.update([f"space-x-{n_str}", f"space-y-{n_str}"])

    # Width & Height
    classes.update(["w-auto", "w-full", "w-screen", "h-auto", "h-full", "h-screen"])
    for n in [0, 1, 2, 3, 4, 6, 8, 12, 16, 20, 24, 32, 40, 48, 56, 64]:
        classes.update([f"w-{n}", f"h-{n}"])

    # Typography
    for size in TEXT_SIZES:
        classes.add(f"text-{size}")
    for weight in FONT_WEIGHTS:
        classes.add(f"font-{weight}")
    classes.update(["text-left", "text-center", "text-right", "text-justify"])
    classes.update(["italic", "not-italic", "uppercase", "lowercase", "capitalize", "normal-case"])
    classes.update(["underline", "line-through", "no-underline"])

    # Colors (text, background, border)
    for color in COLORS:
        for shade in SHADES:
            classes.add(f"text-{color}-{shade}")
            classes.add(f"bg-{color}-{shade}")
            classes.add(f"border-{color}-{shade}")

    # Opacity
    for opacity in OPACITY:
        classes.add(f"opacity-{opacity}")

    # Borders & Rounded
    for width in BORDER_WIDTH:
        classes.add(f"border-{width}" if width > 0 else "border")
    for rounded in ROUNDED:
        classes.add(f"rounded-{rounded}" if rounded else "rounded")

    # Shadows
    classes.update(["shadow-sm", "shadow", "shadow-md", "shadow-lg", "shadow-xl", "shadow-2xl", "shadow-none"])

    # Transitions & Transforms
    classes.update(["transition", "transition-all", "transition-colors", "transition-opacity", "transition-transform"])
    classes.update(["duration-75", "duration-100", "duration-150", "duration-200", "duration-300", "duration-500", "duration-700", "duration-1000"])
    classes.update(["ease-linear", "ease-in", "ease-out", "ease-in-out"])
    classes.update(["scale-0", "scale-50", "scale-75", "scale-90", "scale-95", "scale-100", "scale-105", "scale-110", "scale-125", "scale-150"])
    classes.update(["rotate-0", "rotate-45", "rotate-90", "rotate-180"])

    # Responsive prefixes - sample a few
    for cls in list(classes)[:50]:  # Don't duplicate everything, just sample
        classes.add(f"sm:{cls}")
        classes.add(f"md:{cls}")
        classes.add(f"lg:{cls}")

    # Hover/focus states - sample a few
    for cls in list(classes)[:50]:
        classes.add(f"hover:{cls}")
        classes.add(f"focus:{cls}")

    return sorted(classes)

def create_html_with_tailwind(tailwind_js, test_classes):
    """Create an HTML file that loads Tailwind and uses test classes"""
    classes_html = " ".join(test_classes)

    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tailwind Test</title>
    <script>{tailwind_js}</script>
</head>
<body>
    <!-- Div with all test classes -->
    <div class="{classes_html}">
        Test content
    </div>

    <script>
        // Wait for Tailwind to process
        setTimeout(() => {{
            // Find the generated style tag
            const styleTag = document.querySelector('style');
            if (styleTag) {{
                console.log('TAILWIND_CSS_START');
                console.log(styleTag.textContent);
                console.log('TAILWIND_CSS_END');
            }}
        }}, 1000);
    </script>
</body>
</html>"""
    return html

def extract_css_from_html(html_content):
    """Execute HTML with Tailwind and extract generated CSS using Node.js with happy-dom"""
    # Use vite directory where happy-dom is installed
    vite_dir = Path("vite")
    if not vite_dir.exists():
        vite_dir.mkdir()

    # Write HTML file to vite directory
    html_file = vite_dir / "tailwind_test.html"
    html_file.write_text(html_content)

    # Create a Node.js script using happy-dom (lightweight DOM implementation)
    node_script = vite_dir / "extract_css.mjs"
    node_script.write_text(f"""
import {{ Window }} from 'happy-dom';
import {{ readFileSync }} from 'fs';

const html = readFileSync('{html_file.name}', 'utf8');
const window = new Window({{ url: 'http://localhost' }});
const document = window.document;

// Parse and load HTML properly
document.documentElement.innerHTML = html;

// Make global objects available for Tailwind
global.window = window;
global.document = document;

// Execute the script tags
const scripts = document.querySelectorAll('script');
for (const script of scripts) {{
    if (script.textContent) {{
        try {{
            eval(script.textContent);
        }} catch (e) {{
            console.error('Error executing script:', e.message);
        }}
    }}
}}

// Wait for Tailwind to process
await new Promise(resolve => setTimeout(resolve, 3000));

const styleTag = document.querySelector('style');
if (styleTag) {{
    console.log(styleTag.textContent);
}} else {{
    console.error('No style tag found');
    console.error('Head content:', document.head.innerHTML.slice(0, 500));
    process.exit(1);
}}

process.exit(0);
""")

    # Run with Node.js from vite directory
    try:
        result = subprocess.run(
            ['node', node_script.name],
            cwd=str(vite_dir),
            capture_output=True,
            text=True,
            timeout=20
        )
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            print(f"Node.js error: {result.stderr}")
            print("To install happy-dom: cd vite && npm install happy-dom")
            return None
    except FileNotFoundError:
        print("Node.js not found.")
        return None
    except Exception as e:
        print(f"Error running Node.js: {e}")
        return None

def parse_css_for_classes(css_content):
    """Extract class names from CSS content"""
    classes = set()

    # Match class selectors like .class-name
    # This regex looks for . followed by class name, avoiding pseudo-classes and media queries
    class_pattern = r'\.([a-zA-Z0-9_-]+(?:\\[a-zA-Z0-9_-]+)?)'

    matches = re.findall(class_pattern, css_content)

    for match in matches:
        # Clean up escaped characters (Tailwind escapes special chars like :)
        clean_class = match.replace('\\\\', '')

        # Skip common pseudo-classes and special cases
        if not any(skip in clean_class for skip in ['hover', 'focus', 'active', 'visited', 'disabled', 'first', 'last', 'odd', 'even']):
            classes.add(clean_class)

    # Also handle variant selectors like .sm\:flex -> sm:flex
    variant_pattern = r'\\.((?:[a-z0-9]+\\\\:)+[a-zA-Z0-9_-]+)'
    variant_matches = re.findall(variant_pattern, css_content)
    for match in variant_matches:
        clean_class = match.replace('\\\\:', ':')
        classes.add(clean_class)

    return sorted(classes)

def generate_tailwind_contract():
    """Main function to generate the Tailwind class contract file"""

    print("Step 1: Downloading Tailwind browser bundle...")
    tailwind_js = download_tailwind_bundle()
    print(f"Downloaded {len(tailwind_js)} characters")

    print("\nStep 2: Generating test classes...")
    test_classes = generate_test_classes()
    print(f"Generated {len(test_classes)} test classes")

    print("\nStep 3: Creating HTML with Tailwind...")
    html_content = create_html_with_tailwind(tailwind_js, test_classes)

    print("\nStep 4: Executing and extracting CSS...")
    css_content = extract_css_from_html(html_content)

    if not css_content:
        print("Failed to extract CSS. Please ensure Node.js and jsdom are installed.")
        print("To install jsdom: cd vite && npm install jsdom")
        return None

    print(f"Extracted {len(css_content)} characters of CSS")

    print("\nStep 5: Parsing CSS for class names...")
    class_names = parse_css_for_classes(css_content)
    print(f"Found {len(class_names)} unique classes")

    print("\nStep 6: Writing to tailwind_contract.txt...")
    output_file = Path("tailwind_contract.txt")
    output_file.write_text("\n".join(class_names))
    print(f"Wrote {len(class_names)} classes to {output_file}")

    return class_names

if __name__ == "__main__":
    classes = generate_tailwind_contract()
    if classes:
        print(f"\nSuccess! Generated contract with {len(classes)} classes")
        print("\nFirst 20 classes:")
        for cls in classes[:20]:
            print(f"  {cls}")
