# DaisyUI Theme System Documentation

## Overview

DaisyUI provides 32 pre-built themes with a comprehensive color system using OKLCH color space. Each theme includes semantic colors, layout properties, and design tokens optimized for UI components.

## Color System

### OKLCH Color Space
DaisyUI uses **OKLCH (Oklab Lightness Chroma Hue)** for all colors:
- Format: `oklch(L% C H)` where:
  - L = Lightness (0-100%)
  - C = Chroma (0-0.4, unbounded but typically < 0.4)
  - H = Hue (0-360 degrees)
- Benefits: Perceptually uniform, better color interpolation, predictable contrast

### Color Variables

Each theme defines these color properties:

#### Base Colors
- `--color-base-100`: Primary background
- `--color-base-200`: Secondary background (slightly darker/lighter)
- `--color-base-300`: Tertiary background (more contrast)
- `--color-base-content`: Text color for base backgrounds

#### Semantic Colors
Each semantic color has a main color and a content color for text:
- `--color-primary` / `--color-primary-content`: Main brand color
- `--color-secondary` / `--color-secondary-content`: Secondary brand color
- `--color-accent` / `--color-accent-content`: Accent/highlight color
- `--color-neutral` / `--color-neutral-content`: Neutral gray color

#### State Colors
- `--color-info` / `--color-info-content`: Information messages
- `--color-success` / `--color-success-content`: Success states
- `--color-warning` / `--color-warning-content`: Warning messages
- `--color-error` / `--color-error-content`: Error states

### Design Tokens

#### Border Radius
- `--radius-selector`: Radius for selectable elements (buttons, inputs)
- `--radius-field`: Radius for form fields
- `--radius-box`: Radius for boxes/cards

#### Sizing
- `--size-selector`: Size modifier for selectable elements
- `--size-field`: Size modifier for form fields

#### Visual Properties
- `--border`: Border width (typically 1px)
- `--depth`: Shadow depth level (0-5)
- `--noise`: Noise texture level (0-1)

## Theme Categories

### Light Themes (11)
1. **light** - Clean, minimal light theme
2. **cupcake** - Soft pastel colors
3. **bumblebee** - Yellow/amber accents
4. **emerald** - Green nature theme
5. **corporate** - Professional blue theme
6. **valentine** - Pink/red romantic theme
7. **garden** - Fresh green theme
8. **lofi** - Low contrast, paper-like
9. **pastel** - Soft, muted colors
10. **fantasy** - Whimsical, playful colors
11. **wireframe** - Black and white only

### Dark Themes (11)
1. **dark** - Standard dark theme
2. **synthwave** - Neon 80s aesthetic
3. **halloween** - Orange and purple
4. **forest** - Deep green forest
5. **black** - Pure black background
6. **luxury** - Gold on black
7. **dracula** - Popular Dracula theme
8. **night** - Deep blue night sky
9. **coffee** - Brown coffee tones
10. **dim** - Dimmed dark theme
11. **business** - Professional dark

### High Contrast Themes (5)
1. **cyberpunk** - High contrast neon
2. **aqua** - Cyan/blue water theme
3. **acid** - Bright, vivid colors
4. **lemonade** - Yellow/green citrus
5. **retro** - Retro computing aesthetic

### Specialty Themes (5)
1. **cmyk** - Print-inspired colors
2. **autumn** - Fall color palette
3. **winter** - Cool blues and whites
4. **nord** - Popular Nord palette
5. **sunset** - Orange/purple gradient

## Theme Application

### HTML Attribute
```html
<html data-theme="dark">
```

### CSS Class
```html
<div data-theme="cupcake">
  <!-- Content uses cupcake theme -->
</div>
```

### Theme Controller (Form Input)
```html
<input type="radio" name="theme-controller" value="dark" />
```

## Alpha Channel Support

DaisyUI handles alpha channels through CSS properties:
```css
/* These are set dynamically based on theme */
--border-alpha: 0.3;  /* Light themes */
--border-alpha: 0.75; /* Dark themes */
--input-alpha: 0.4;   /* Light themes */
--input-alpha: 0.75;  /* Dark themes */
```

## Example Theme Values

### Light Theme
```css
[data-theme="light"] {
  color-scheme: light;
  --color-base-100: oklch(100% 0 0);        /* Pure white */
  --color-base-content: oklch(21% 0.006 285.885); /* Near black */
  --color-primary: oklch(45% 0.24 277.023);  /* Blue */
  --color-secondary: oklch(65% 0.241 354.308); /* Pink */
  --color-accent: oklch(77% 0.152 181.912);  /* Teal */
  --color-success: oklch(76% 0.177 163.223); /* Green */
  --color-warning: oklch(82% 0.189 84.429);  /* Yellow */
  --color-error: oklch(71% 0.194 13.428);    /* Red */
}
```

### Dark Theme
```css
[data-theme="dark"] {
  color-scheme: dark;
  --color-base-100: oklch(25.33% 0.016 252.42); /* Dark blue-gray */
  --color-base-content: oklch(97.807% 0.029 256.847); /* Near white */
  --color-primary: oklch(58% 0.233 277.117);  /* Bright blue */
  --color-secondary: oklch(65% 0.241 354.308); /* Pink */
  --color-accent: oklch(77% 0.152 181.912);   /* Teal */
  --color-success: oklch(76% 0.177 163.223);  /* Green */
  --color-warning: oklch(82% 0.189 84.429);   /* Yellow */
  --color-error: oklch(71% 0.194 13.428);     /* Red */
}
```

### Synthwave Theme (Unique Example)
```css
[data-theme="synthwave"] {
  color-scheme: dark;
  --color-base-100: oklch(25.98% 0.064 276.7); /* Deep purple */
  --color-primary: oklch(94.45% 0.197 336.36); /* Hot pink */
  --color-secondary: oklch(84.22% 0.236 112.23); /* Neon yellow */
  --color-accent: oklch(76.61% 0.239 192.75); /* Cyan */
  /* Neon glow effect through high chroma values */
}
```

## Component Theming

DaisyUI components automatically use theme variables:
- Buttons use `--color-primary` for `.btn-primary`
- Alerts use semantic colors (`info`, `success`, `warning`, `error`)
- Cards use `--color-base-100` for backgrounds
- Text uses `--color-base-content` by default

## Theme Switching Implementation

### JavaScript Theme Switcher
```javascript
// Get current theme
const currentTheme = document.documentElement.getAttribute('data-theme');

// Set new theme
document.documentElement.setAttribute('data-theme', 'dark');

// Store preference
localStorage.setItem('theme', 'dark');

// Load saved theme on page load
const savedTheme = localStorage.getItem('theme') || 'light';
document.documentElement.setAttribute('data-theme', savedTheme);
```

### Theme Toggle Component
```html
<label class="swap swap-rotate">
  <input type="checkbox" class="theme-controller" value="dark" />
  <svg class="swap-on"><!-- Sun icon --></svg>
  <svg class="swap-off"><!-- Moon icon --></svg>
</label>
```

## Color Contrast

DaisyUI ensures WCAG compliance by:
- Pairing each color with an appropriate `content` color
- Using OKLCH for predictable contrast ratios
- Providing high-contrast theme options

## Theme Customization

### Creating Custom Themes
```css
[data-theme="custom"] {
  --color-primary: oklch(65% 0.3 275);
  --color-secondary: oklch(60% 0.25 60);
  /* Define all required variables */
}
```

### Extending Existing Themes
```css
[data-theme="mytheme"] {
  /* Inherit from light theme */
  @extend [data-theme="light"];
  /* Override specific colors */
  --color-primary: oklch(50% 0.3 250);
}
```

## Complete Theme List with Primary Colors

| Theme | Primary Color | Base Background | Color Scheme |
|-------|--------------|-----------------|--------------|
| light | oklch(45% 0.24 277) | oklch(100% 0 0) | light |
| dark | oklch(58% 0.233 277) | oklch(25.33% 0.016 252) | dark |
| cupcake | oklch(65% 0.163 288) | oklch(98% 0.04 161) | light |
| bumblebee | oklch(81% 0.169 80) | oklch(100% 0 0) | light |
| emerald | oklch(58% 0.216 162) | oklch(100% 0 0) | light |
| corporate | oklch(47% 0.17 262) | oklch(100% 0 0) | light |
| synthwave | oklch(94% 0.197 336) | oklch(26% 0.064 277) | dark |
| retro | oklch(74% 0.152 66) | oklch(92% 0.034 100) | light |
| cyberpunk | oklch(81% 0.195 90) | oklch(100% 0 0) | light |
| valentine | oklch(81% 0.195 356) | oklch(98% 0.052 343) | light |
| halloween | oklch(81% 0.195 47) | oklch(24% 0.026 256) | dark |
| garden | oklch(58% 0.235 150) | oklch(99% 0.027 191) | light |
| forest | oklch(58% 0.216 162) | oklch(21% 0.019 131) | dark |
| aqua | oklch(75% 0.216 218) | oklch(100% 0 0) | light |
| lofi | oklch(45% 0.026 301) | oklch(100% 0 0) | light |
| pastel | oklch(64% 0.2 335) | oklch(100% 0 0) | light |
| fantasy | oklch(81% 0.195 356) | oklch(100% 0 0) | light |
| wireframe | oklch(29% 0 0) | oklch(100% 0 0) | light |
| black | oklch(100% 0 0) | oklch(0% 0 0) | dark |
| luxury | oklch(76% 0.131 70) | oklch(14% 0.008 282) | dark |
| dracula | oklch(81% 0.195 356) | oklch(29% 0 0) | dark |
| cmyk | oklch(74% 0.16 232) | oklch(100% 0 0) | light |
| autumn | oklch(65% 0.241 354) | oklch(99% 0.014 89) | light |
| business | oklch(47% 0.17 262) | oklch(24% 0.019 238) | dark |
| acid | oklch(83% 0.195 90) | oklch(99% 0.009 121) | light |
| lemonade | oklch(84% 0.169 80) | oklch(98% 0.028 93) | light |
| night | oklch(56% 0.278 262) | oklch(19% 0.041 246) | dark |
| coffee | oklch(51% 0.11 53) | oklch(23% 0.044 48) | dark |
| winter | oklch(53% 0.261 269) | oklch(100% 0 0) | light |
| dim | oklch(59% 0.233 277) | oklch(21% 0.024 239) | dark |
| nord | oklch(64% 0.112 242) | oklch(26% 0.019 241) | dark |
| sunset | oklch(71% 0.195 47) | oklch(21% 0.042 250) | dark |