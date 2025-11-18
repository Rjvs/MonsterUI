# Tailwind CSS v4 Theme System Documentation

## Overview

Tailwind CSS v4 introduces a new theme system using CSS custom properties (CSS variables) defined in the `@theme` layer. This provides a comprehensive design system with colors, spacing, typography, shadows, and other design tokens.

## Color System

### Color Format
Tailwind v4 uses **OKLCH color space** for all colors:
- Format: `oklch(L% C H)` 
- Benefits: Perceptually uniform, better gradients, predictable lightness

### Color Palette Structure

Each color has 11 shades (50-950):
- **50**: Lightest tint
- **100-400**: Light shades
- **500**: Base color (mid-point)
- **600-900**: Dark shades
- **950**: Darkest shade

### Available Color Scales

#### Neutral Colors (5 scales)
1. **slate**: Cool gray with blue undertone
2. **gray**: True neutral gray
3. **zinc**: Cool gray with slight blue
4. **neutral**: Pure achromatic gray
5. **stone**: Warm gray with brown undertone

#### Primary Colors (15 scales)
1. **red**: True red
2. **orange**: Vibrant orange
3. **amber**: Warm amber/gold
4. **yellow**: Bright yellow
5. **lime**: Yellow-green
6. **green**: True green
7. **emerald**: Blue-green
8. **teal**: Blue-green cyan
9. **cyan**: True cyan
10. **sky**: Light blue
11. **blue**: True blue
12. **indigo**: Deep blue-purple
13. **violet**: Blue-purple
14. **purple**: True purple
15. **fuchsia**: Pink-purple
16. **pink**: True pink
17. **rose**: Red-pink

### Example Color Values

#### Blue Scale
```css
--color-blue-50: oklch(97% 0.014 254.604);
--color-blue-100: oklch(93.2% 0.032 255.585);
--color-blue-200: oklch(88.2% 0.059 254.128);
--color-blue-300: oklch(80.9% 0.105 251.813);
--color-blue-400: oklch(70.7% 0.165 254.624);
--color-blue-500: oklch(62.3% 0.214 259.815);  /* Base blue */
--color-blue-600: oklch(54.6% 0.245 262.881);
--color-blue-700: oklch(48.8% 0.243 264.376);
--color-blue-800: oklch(42.4% 0.199 265.638);
--color-blue-900: oklch(37.9% 0.146 265.522);
--color-blue-950: oklch(28.2% 0.091 267.935);
```

## Design Tokens

### Spacing System
```css
--spacing: 0.25rem; /* Base unit (4px at 16px base) */
/* Spacing scale: 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 72, 80, 96 */
```

### Typography

#### Font Families
```css
--font-sans: ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
--font-serif: ui-serif, Georgia, Cambria, "Times New Roman", Times, serif;
--font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
```

#### Font Sizes
```css
--text-xs: 0.75rem;     /* 12px */
--text-sm: 0.875rem;    /* 14px */
--text-base: 1rem;      /* 16px */
--text-lg: 1.125rem;    /* 18px */
--text-xl: 1.25rem;     /* 20px */
--text-2xl: 1.5rem;     /* 24px */
--text-3xl: 1.875rem;   /* 30px */
--text-4xl: 2.25rem;    /* 36px */
--text-5xl: 3rem;       /* 48px */
--text-6xl: 3.75rem;    /* 60px */
--text-7xl: 4.5rem;     /* 72px */
--text-8xl: 6rem;       /* 96px */
--text-9xl: 8rem;       /* 128px */
```

#### Font Weights
```css
--font-weight-thin: 100;
--font-weight-extralight: 200;
--font-weight-light: 300;
--font-weight-normal: 400;
--font-weight-medium: 500;
--font-weight-semibold: 600;
--font-weight-bold: 700;
--font-weight-extrabold: 800;
--font-weight-black: 900;
```

#### Line Heights
```css
--leading-tight: 1.25;
--leading-snug: 1.375;
--leading-normal: 1.5;
--leading-relaxed: 1.625;
--leading-loose: 2;
```

#### Letter Spacing
```css
--tracking-tighter: -0.05em;
--tracking-tight: -0.025em;
--tracking-normal: 0em;
--tracking-wide: 0.025em;
--tracking-wider: 0.05em;
--tracking-widest: 0.1em;
```

### Border Radius
```css
--radius-xs: 0.125rem;  /* 2px */
--radius-sm: 0.25rem;   /* 4px */
--radius-md: 0.375rem;  /* 6px */
--radius-lg: 0.5rem;    /* 8px */
--radius-xl: 0.75rem;   /* 12px */
--radius-2xl: 1rem;     /* 16px */
--radius-3xl: 1.5rem;   /* 24px */
--radius-4xl: 2rem;     /* 32px */
```

### Shadows

#### Box Shadows
```css
--shadow-2xs: 0 1px rgb(0 0 0 / 0.05);
--shadow-xs: 0 1px 2px 0 rgb(0 0 0 / 0.05);
--shadow-sm: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);
--shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
--shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
--shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
--shadow-2xl: 0 25px 50px -12px rgb(0 0 0 / 0.25);
```

#### Inset Shadows
```css
--inset-shadow-2xs: inset 0 1px rgb(0 0 0 / 0.05);
--inset-shadow-xs: inset 0 1px 1px rgb(0 0 0 / 0.05);
--inset-shadow-sm: inset 0 2px 4px rgb(0 0 0 / 0.05);
```

#### Drop Shadows
```css
--drop-shadow-xs: 0 1px 1px rgb(0 0 0 / 0.05);
--drop-shadow-sm: 0 1px 2px rgb(0 0 0 / 0.15);
--drop-shadow-md: 0 3px 3px rgb(0 0 0 / 0.12);
--drop-shadow-lg: 0 4px 4px rgb(0 0 0 / 0.15);
--drop-shadow-xl: 0 9px 7px rgb(0 0 0 / 0.1);
--drop-shadow-2xl: 0 25px 25px rgb(0 0 0 / 0.15);
```

#### Text Shadows
```css
--text-shadow-2xs: 0px 1px 0px rgb(0 0 0 / 0.15);
--text-shadow-xs: 0px 1px 1px rgb(0 0 0 / 0.2);
--text-shadow-sm: 0px 1px 0px rgb(0 0 0 / 0.075), 0px 1px 1px rgb(0 0 0 / 0.075), 0px 2px 2px rgb(0 0 0 / 0.075);
--text-shadow-md: 0px 1px 1px rgb(0 0 0 / 0.1), 0px 1px 2px rgb(0 0 0 / 0.1), 0px 2px 4px rgb(0 0 0 / 0.1);
--text-shadow-lg: 0px 1px 2px rgb(0 0 0 / 0.1), 0px 3px 2px rgb(0 0 0 / 0.1), 0px 4px 8px rgb(0 0 0 / 0.1);
```

### Breakpoints
```css
--breakpoint-sm: 40rem;   /* 640px */
--breakpoint-md: 48rem;   /* 768px */
--breakpoint-lg: 64rem;   /* 1024px */
--breakpoint-xl: 80rem;   /* 1280px */
--breakpoint-2xl: 96rem;  /* 1536px */
```

### Container Sizes
```css
--container-3xs: 16rem;   /* 256px */
--container-2xs: 18rem;   /* 288px */
--container-xs: 20rem;    /* 320px */
--container-sm: 24rem;    /* 384px */
--container-md: 28rem;    /* 448px */
--container-lg: 32rem;    /* 512px */
--container-xl: 36rem;    /* 576px */
--container-2xl: 42rem;   /* 672px */
--container-3xl: 48rem;   /* 768px */
--container-4xl: 56rem;   /* 896px */
--container-5xl: 64rem;   /* 1024px */
--container-6xl: 72rem;   /* 1152px */
--container-7xl: 80rem;   /* 1280px */
```

### Animation

#### Timing Functions
```css
--ease-in: cubic-bezier(0.4, 0, 1, 1);
--ease-out: cubic-bezier(0, 0, 0.2, 1);
--ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
```

#### Default Animations
```css
--animate-spin: spin 1s linear infinite;
--animate-ping: ping 1s cubic-bezier(0, 0, 0.2, 1) infinite;
--animate-pulse: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
--animate-bounce: bounce 1s infinite;
```

### Effects

#### Blur
```css
--blur-xs: 4px;
--blur-sm: 8px;
--blur-md: 12px;
--blur-lg: 16px;
--blur-xl: 24px;
--blur-2xl: 40px;
--blur-3xl: 64px;
```

#### Perspective
```css
--perspective-dramatic: 100px;
--perspective-near: 300px;
--perspective-normal: 500px;
--perspective-midrange: 800px;
--perspective-distant: 1200px;
```

### Aspect Ratios
```css
--aspect-video: 16 / 9;
```

### Default Transitions
```css
--default-transition-duration: 150ms;
--default-transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
```

## Theme Usage

### Using CSS Variables
```css
/* Direct usage */
.my-element {
  background-color: oklch(var(--color-blue-500));
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
}
```

### Using Tailwind Classes
```html
<!-- These classes reference the CSS variables -->
<div class="bg-blue-500 rounded-lg shadow-md">
  <p class="text-gray-700 text-lg font-semibold">Content</p>
</div>
```

## Dark Mode Support

Tailwind v4 doesn't have built-in dark mode themes, but supports dark mode through:

1. **CSS Class Strategy**
```css
.dark {
  /* Custom dark mode overrides */
}
```

2. **Media Query Strategy**
```css
@media (prefers-color-scheme: dark) {
  /* Dark mode styles */
}
```

3. **Custom Properties Override**
```css
.dark {
  --color-background: var(--color-gray-900);
  --color-foreground: var(--color-gray-100);
}
```

## Customization

### Extending the Theme
```css
@theme {
  /* Add custom variables */
  --color-brand: oklch(60% 0.25 250);
  --spacing-custom: 1.75rem;
  --radius-custom: 0.625rem;
}
```

### Overriding Variables
```css
:root {
  /* Override default values */
  --color-blue-500: oklch(55% 0.3 250);
  --font-sans: "Inter", system-ui, sans-serif;
}
```

## Key Differences from Other Systems

1. **No Pre-defined Themes**: Unlike DaisyUI, Tailwind provides design tokens but not complete themes
2. **OKLCH Color Space**: Modern perceptually uniform color system
3. **Utility-First**: Designed for atomic utility classes
4. **CSS Variables**: All values exposed as CSS custom properties
5. **Comprehensive Scale**: Extensive range of values for each property

## Integration with MonsterUI

In MonsterUI context, Tailwind provides:
- Base design tokens and scales
- Utility classes for layout and spacing
- Typography system
- Shadow and effect utilities
- Responsive design breakpoints

The other libraries (FrankenUI and DaisyUI) build themed components on top of these foundational design tokens.