# FrankenUI Theme System Documentation

## Overview

FrankenUI provides a comprehensive theming system with 15 color themes, each available in light and dark modes, resulting in 30 total theme variations. The system uses HSL color values and CSS custom properties for dynamic theming.

## Theme Application

Themes are applied using CSS classes on the HTML element:
- Color theme: `uk-theme-{color}` (e.g., `uk-theme-blue`)
- Dark mode: `dark` class
- Additional modifiers: `uk-radii-{size}`, `uk-shadows-{size}`, `uk-font-{size}`

## Available Themes

### Color Themes (15 total)
1. **Neutral Grays**
   - `zinc` - Cool gray with slight blue undertone
   - `slate` - Blue-gray theme
   - `gray` - True neutral gray
   - `neutral` - Pure achromatic gray
   - `stone` - Warm gray with brown undertone

2. **Primary Colors**
   - `blue` - Primary blue theme
   - `red` - Vibrant red theme
   - `green` - Nature green theme
   - `orange` - Energetic orange theme
   - `yellow` - Bright yellow theme

3. **Extended Colors**
   - `violet` - Deep violet theme
   - `purple` - Royal purple theme
   - `rose` - Soft rose/pink theme
   - `amber` - Warm amber/gold theme
   - `teal` - Blue-green teal theme

## CSS Variables Structure

Each theme defines the following CSS custom properties:

### Core Color Variables
- `--background`: Main background color (HSL)
- `--foreground`: Main text color (HSL)
- `--card`: Card background color
- `--card-foreground`: Card text color
- `--popover`: Popover background color
- `--popover-foreground`: Popover text color

### Semantic Colors
- `--primary`: Primary brand color
- `--primary-foreground`: Text on primary color
- `--secondary`: Secondary color
- `--secondary-foreground`: Text on secondary color
- `--accent`: Accent color for highlights
- `--accent-foreground`: Text on accent color
- `--muted`: Muted/subdued color
- `--muted-foreground`: Text on muted backgrounds
- `--destructive`: Error/danger color
- `--destructive-foreground`: Text on destructive color

### UI Element Colors
- `--border`: Border color
- `--input`: Input field border/background
- `--ring`: Focus ring color

### Component-Specific Variables
- `--uk-form-checkbox-image`: SVG data URL for checkbox checked state
- `--uk-form-checkbox-image-indeterminate`: SVG for indeterminate state
- `--uk-form-radio-image`: SVG for radio button selected state
- `--uk-form-list-image`: SVG for select dropdown arrow
- `--uk-divider-icon-image`: SVG for divider decoration
- `--uk-list-bullet-image`: SVG for list bullets

## Color Format

FrankenUI uses **HSL (Hue, Saturation, Lightness)** format for all color values:
- Format: `H S% L%` (e.g., `221.2 83.2% 53.3%`)
- No commas between values
- Applied using `hsl()` function in CSS

## Example Theme Values

### Blue Theme (Light Mode)
```css
.uk-theme-blue {
  --background: 0 0% 100%;           /* white */
  --foreground: 0 0% 4%;             /* near black */
  --primary: 221.2 83.2% 53.3%;      /* blue */
  --primary-foreground: 213.8 100% 96.9%; /* light blue */
  --secondary: 0 0% 96%;             /* light gray */
  --accent: 0 0% 96%;                /* light gray */
  --destructive: 357 100% 45%;       /* red */
  --border: 0 0% 90%;                /* light gray */
  --input: 0 0% 90%;                 /* light gray */
  --ring: 213.1 93.9% 67.8%;         /* light blue */
}
```

### Blue Theme (Dark Mode)
```css
.dark.uk-theme-blue {
  --background: 0 0% 4%;             /* near black */
  --foreground: 0 0% 98%;            /* near white */
  --primary: 217.2 91.2% 59.8%;      /* blue */
  --primary-foreground: 213.8 100% 96.9%; /* light blue */
  --secondary: 0 0% 15%;             /* dark gray */
  --accent: 0 0% 25%;                /* gray */
  --destructive: 357 100% 45%;       /* red */
  --border: 0 0% 100%;               /* white */
  --input: 0 0% 100%;                /* white */
  --ring: 224.4 64.3% 32.9%;         /* dark blue */
}
```

## Dark Mode Implementation

Dark mode is controlled by:
1. Adding the `dark` class to the HTML element
2. Each theme has specific dark mode overrides
3. Component images (checkboxes, radios) adjust for dark backgrounds

## Alpha Channel Support

FrankenUI also supports alpha channel adjustments for borders and inputs:
```javascript
const borderAlpha = isDark ? "0.75" : "0.3";
const inputAlpha = isDark ? "0.75" : "0.4";
htmlElement.style.setProperty("--border-alpha", borderAlpha);
htmlElement.style.setProperty("--input-alpha", inputAlpha);
```

## Theme Storage

Themes are persisted in localStorage under the `__FRANKEN__` key:
```javascript
{
  "mode": "dark" | "light",
  "theme": "uk-theme-blue",
  "radii": "uk-radii-sm",
  "shadows": "uk-shadows-sm",
  "font": "uk-font-sm"
}
```

## Integration with UIkit

FrankenUI themes are built on top of UIkit's component system and inherit all UIkit CSS variables for:
- Breakpoints (`--uk-breakpoint-s/m/l/xl`)
- Global styles (`--uk-global-*`)
- Component-specific variables (`--uk-btn-*`, `--uk-form-*`, etc.)

## Theme Switching

To switch themes programmatically:
```javascript
// Remove current theme
document.documentElement.classList.remove('uk-theme-blue');
// Add new theme
document.documentElement.classList.add('uk-theme-green');
// Toggle dark mode
document.documentElement.classList.toggle('dark');
```

## Complete Theme List

All 15 themes with their primary distinguishing colors:

| Theme | Primary Color (Light) | Primary Color (Dark) |
|-------|----------------------|---------------------|
| zinc | 240 5.9% 10% | 0 0% 98% |
| slate | 222.2 47.4% 11.2% | 210 40% 96.1% |
| gray | 220.9 39.3% 11% | 210 20% 98% |
| neutral | 0 0% 9% | 0 0% 90% |
| blue | 221.2 83.2% 53.3% | 217.2 91.2% 59.8% |
| red | 0 72.2% 50.6% | 0 84.2% 60.2% |
| green | 142.1 76.2% 36.3% | 142.1 70.6% 45.3% |
| orange | 24.6 95% 53.1% | 20.5 90.2% 48.2% |
| yellow | 47.9 95.8% 53.1% | 47.9 95.8% 53.1% |
| violet | 263.4 90% 51% | 263.4 90% 51% |
| purple | 267.1 84.8% 60.1% | 270.7 91% 65.1% |
| rose | 346.8 77.2% 49.8% | 346.8 77.2% 49.8% |
| amber | 37.7 92.1% 50.2% | 45.4 93.4% 47.5% |
| teal | 172.7 66% 50.6% | 172.7 66% 50.6% |
| stone | 24.6 5.4% 63.9% | 33.3 5.5% 32.4% |