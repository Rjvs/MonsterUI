# MonsterUI Integrated CSS Build System

This Vite-based build system successfully integrates Tailwind CSS 4, FrankenUI 2.1.1, and DaisyUI 5 into a unified CSS bundle for the MonsterUI framework.

## Integration Strategy

### Problem Solved
Previously, these three libraries conflicted due to:
- CSS layer conflicts and specificity issues
- Processing order problems
- Variable namespace collisions 
- DaisyUI's global base styles clobbering Tailwind and FrankenUI

### Solution Implemented
1. **PostCSS Pipeline**: Advanced CSS processing with custom plugins for scoping and isolation
2. **Proper Layering**: Explicit CSS layer management to control cascade order
3. **Scope Isolation**: DaisyUI limited to `[data-theme]` elements to prevent global conflicts
4. **Variable Namespacing**: CSS custom properties isolated to prevent collisions
5. **Plugin Orchestration**: Careful ordering of Vite plugins for proper processing

## Architecture

### CSS Processing Order
1. **Tailwind Base** → Foundation styles and reset
2. **FrankenUI Components** → UIKit-based component library (via Vite plugin)
3. **DaisyUI Components** → Scoped to `[data-theme]` elements
4. **Utilities** → All utility classes from all libraries

### Files Generated
- `monsterui.css` (483KB) - Complete integrated stylesheet
- `monsterui-core.js` (238KB) - FrankenUI core functionality  
- `monsterui-icons.js` (383KB) - FrankenUI icon system
- `monsterui-rte.js` (343KB) - FrankenUI rich text editor

## Usage

### Development
```bash
npm run dev    # Start development server at http://localhost:5173
```

### Production Build
```bash
npm run build  # Generate assets in /outputs directory
```

### In MonsterUI Applications
```html
<!-- Include the integrated CSS -->
<link rel="stylesheet" href="path/to/monsterui.css">

<!-- Include FrankenUI JavaScript for interactive components -->
<script src="path/to/monsterui-core.js"></script>
<script src="path/to/monsterui-icons.js"></script>
<script src="path/to/monsterui-rte.js"></script>

<!-- Use Tailwind utilities everywhere -->
<div class="flex items-center space-x-4">

<!-- Use FrankenUI components with uk- prefix -->
<button class="uk-btn uk-btn-primary">FrankenUI Button</button>

<!-- Use DaisyUI components within data-theme containers -->
<div data-theme="light">
  <button class="btn btn-primary">DaisyUI Button</button>
</div>
```

## Library Coexistence

### Tailwind CSS 4
- **Scope**: Global utilities and base styles
- **Usage**: Standard utility classes (flex, p-4, bg-blue-500, etc.)
- **Conflicts**: None - serves as foundation

### FrankenUI 2.1.1
- **Scope**: Global components with `uk-` prefix  
- **Usage**: UIKit-style components (uk-btn, uk-card, uk-modal, etc.)
- **Conflicts**: None - isolated by prefix and proper layering

### DaisyUI 5
- **Scope**: Components within `[data-theme]` containers
- **Usage**: Semantic components (btn, card, modal, etc.) 
- **Conflicts**: Resolved - scoped to prevent global style leakage

## Key Features

✅ **No CSS Conflicts** - All three libraries coexist without style collisions  
✅ **Full Functionality** - All components and utilities available  
✅ **Proper Theming** - DaisyUI themes work correctly when scoped  
✅ **Performance Optimized** - Single CSS bundle, no runtime conflicts  
✅ **Framework Compatible** - Works with MonsterUI's dynamic class generation  

## Testing

Open `test.html` in a browser after running `npm run build` to see all three libraries working together harmoniously. The test page demonstrates:

- Tailwind utility classes
- FrankenUI components (buttons, cards, forms, accordions)
- DaisyUI components (scoped with data-theme)
- Mixed usage scenarios
- Theme switching capabilities

## Technical Notes

- CSS layers ensure proper cascade order
- PostCSS plugins handle scoping and variable isolation
- Vite plugin order is critical for proper processing
- All styles preserved for framework usage (no tree-shaking)
- CSS variables properly namespaced to prevent collisions