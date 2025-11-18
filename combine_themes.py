#!/usr/bin/env python3
import json

# Load the extracted themes
with open('frankenui_themes.json', 'r') as f:
    frankenui_themes = json.load(f)

with open('daisyui_themes.json', 'r') as f:
    daisyui_themes = json.load(f)

# Extract Tailwind theme (partial, focusing on colors)
tailwind_theme = {
    "colors": {
        "slate": {
            "50": "oklch(98.4% 0.003 247.858)",
            "100": "oklch(96.8% 0.007 247.896)",
            "200": "oklch(92.9% 0.013 255.508)",
            "300": "oklch(86.9% 0.022 252.894)",
            "400": "oklch(70.4% 0.04 256.788)",
            "500": "oklch(55.4% 0.046 257.417)",
            "600": "oklch(44.6% 0.043 257.281)",
            "700": "oklch(37.2% 0.044 257.287)",
            "800": "oklch(27.9% 0.041 260.031)",
            "900": "oklch(20.8% 0.042 265.755)",
            "950": "oklch(12.9% 0.042 264.695)"
        },
        "gray": {
            "50": "oklch(98.5% 0.002 247.839)",
            "100": "oklch(96.7% 0.003 264.542)",
            "200": "oklch(92.8% 0.006 264.531)",
            "300": "oklch(87.2% 0.01 258.338)",
            "400": "oklch(70.7% 0.022 261.325)",
            "500": "oklch(55.1% 0.027 264.364)",
            "600": "oklch(44.6% 0.03 256.802)",
            "700": "oklch(37.3% 0.034 259.733)",
            "800": "oklch(27.8% 0.033 256.848)",
            "900": "oklch(21% 0.034 264.665)",
            "950": "oklch(13% 0.028 261.692)"
        },
        "zinc": {
            "50": "oklch(98.5% 0 0)",
            "100": "oklch(96.7% 0.001 286.375)",
            "200": "oklch(92% 0.004 286.32)",
            "300": "oklch(87.1% 0.006 286.286)",
            "400": "oklch(70.5% 0.015 286.067)",
            "500": "oklch(55.2% 0.016 285.938)",
            "600": "oklch(44.2% 0.017 285.786)",
            "700": "oklch(37% 0.013 285.805)",
            "800": "oklch(27.4% 0.006 286.033)",
            "900": "oklch(21% 0.006 285.885)",
            "950": "oklch(14.1% 0.005 285.823)"
        },
        "blue": {
            "50": "oklch(97% 0.014 254.604)",
            "100": "oklch(93.2% 0.032 255.585)",
            "200": "oklch(88.2% 0.059 254.128)",
            "300": "oklch(80.9% 0.105 251.813)",
            "400": "oklch(70.7% 0.165 254.624)",
            "500": "oklch(62.3% 0.214 259.815)",
            "600": "oklch(54.6% 0.245 262.881)",
            "700": "oklch(48.8% 0.243 264.376)",
            "800": "oklch(42.4% 0.199 265.638)",
            "900": "oklch(37.9% 0.146 265.522)",
            "950": "oklch(28.2% 0.091 267.935)"
        },
        "red": {
            "50": "oklch(97.1% 0.013 17.38)",
            "100": "oklch(93.6% 0.032 17.717)",
            "200": "oklch(88.5% 0.062 18.334)",
            "300": "oklch(80.8% 0.114 19.571)",
            "400": "oklch(70.4% 0.191 22.216)",
            "500": "oklch(63.7% 0.237 25.331)",
            "600": "oklch(57.7% 0.245 27.325)",
            "700": "oklch(50.5% 0.213 27.518)",
            "800": "oklch(44.4% 0.177 26.899)",
            "900": "oklch(39.6% 0.141 25.723)",
            "950": "oklch(25.8% 0.092 26.042)"
        },
        "green": {
            "50": "oklch(98.2% 0.018 155.826)",
            "100": "oklch(96.2% 0.044 156.743)",
            "200": "oklch(92.5% 0.084 155.995)",
            "300": "oklch(87.1% 0.15 154.449)",
            "400": "oklch(79.2% 0.209 151.711)",
            "500": "oklch(72.3% 0.219 149.579)",
            "600": "oklch(62.7% 0.194 149.214)",
            "700": "oklch(52.7% 0.154 150.069)",
            "800": "oklch(44.8% 0.119 151.328)",
            "900": "oklch(39.3% 0.095 152.535)",
            "950": "oklch(26.6% 0.065 152.934)"
        }
    },
    "spacing": {
        "base": "0.25rem",
        "scale": ["0", "0.5", "1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "6", "7", "8", "9", "10", 
                  "11", "12", "14", "16", "20", "24", "28", "32", "36", "40", "44", "48", "52", "56", 
                  "60", "64", "72", "80", "96"]
    },
    "typography": {
        "fontFamily": {
            "sans": "ui-sans-serif, system-ui, sans-serif",
            "serif": "ui-serif, Georgia, Cambria, Times, serif",
            "mono": "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
        },
        "fontSize": {
            "xs": "0.75rem",
            "sm": "0.875rem",
            "base": "1rem",
            "lg": "1.125rem",
            "xl": "1.25rem",
            "2xl": "1.5rem",
            "3xl": "1.875rem",
            "4xl": "2.25rem",
            "5xl": "3rem",
            "6xl": "3.75rem",
            "7xl": "4.5rem",
            "8xl": "6rem",
            "9xl": "8rem"
        }
    },
    "borderRadius": {
        "xs": "0.125rem",
        "sm": "0.25rem",
        "md": "0.375rem",
        "lg": "0.5rem",
        "xl": "0.75rem",
        "2xl": "1rem",
        "3xl": "1.5rem",
        "4xl": "2rem"
    },
    "shadows": {
        "2xs": "0 1px rgb(0 0 0 / 0.05)",
        "xs": "0 1px 2px 0 rgb(0 0 0 / 0.05)",
        "sm": "0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1)",
        "md": "0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)",
        "lg": "0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1)",
        "xl": "0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1)",
        "2xl": "0 25px 50px -12px rgb(0 0 0 / 0.25)"
    }
}

# Combine all themes
combined_themes = {
    "metadata": {
        "description": "Complete theme extraction from MonsterUI (FrankenUI, DaisyUI, Tailwind CSS)",
        "frankenui_theme_count": len(frankenui_themes),
        "daisyui_theme_count": len(daisyui_themes),
        "color_formats": {
            "frankenui": "HSL (H S% L%)",
            "daisyui": "OKLCH (oklch(L% C H))",
            "tailwind": "OKLCH (oklch(L% C H))"
        }
    },
    "frankenui": frankenui_themes,
    "daisyui": daisyui_themes,
    "tailwind": tailwind_theme
}

# Save combined themes
with open('theme-extraction.json', 'w') as f:
    json.dump(combined_themes, f, indent=2)

print(f"Combined theme extraction saved to theme-extraction.json")
print(f"- FrankenUI: {len(frankenui_themes)} themes")
print(f"- DaisyUI: {len(daisyui_themes)} themes")
print(f"- Tailwind: Design tokens and color scales")