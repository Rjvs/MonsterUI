import tailwindcss from '@tailwindcss/vite';
import franken from "franken-ui/plugin-vite";
import { defineConfig } from "vite";
import { resolve } from 'path';
import { copyFileSync } from 'fs';

export default defineConfig({
	plugins: [
		franken({
			preflight: false,
			layer: true,
      layerExceptions: ['Icon', 'Spinner', 'SVG'],
		}),
    tailwindcss(),
	],
  optimizeDeps: {
    noDiscovery: true,
    include: []
  },
  // Build configuration for library mode  
  build: {
    outDir: 'outputs',
    cssCodeSplit: false, // Bundle all CSS into one file
    // Disable CSS minification to preserve FrankenUI themes
    cssMinify: false,
    rollupOptions: {
      input: resolve(__dirname, 'index.html'), // CSS entry point only
      output: {
        // Configure asset naming
        assetFileNames: (assetInfo) => {
          if (assetInfo.name && assetInfo.name.endsWith('.css')) {
            return 'monsterui.css'
          }
          return assetInfo.name || 'asset.[ext]'
        },
        entryFileNames: 'index.js', // Dummy JS file (will be minimal)
      }
    },
    // Clear output directory on build
    emptyOutDir: true,
  },
});

// Plugin to copy FrankenUI IIFE bundles
const copyFrankenUIJS = () => ({
  name: 'copy-frankenui-js',
  writeBundle() {
    const sourceDir = resolve(__dirname, 'node_modules/franken-ui/dist/js')
    const outputDir = resolve(__dirname, 'outputs')

    // Copy core functionality
    copyFileSync(
      resolve(sourceDir, 'core.iife.js'),
      resolve(outputDir, 'monsterui-core.js')
    )

    // Copy icons functionality
    copyFileSync(
      resolve(sourceDir, 'icon.iife.js'),
      resolve(outputDir, 'monsterui-icons.js')
    )

    // Copy rich text editor functionality
    copyFileSync(
      resolve(sourceDir, 'rte.iife.js'),
      resolve(outputDir, 'monsterui-rte.js')
    )

    console.log('✓ Copied FrankenUI JS bundles with consistent naming (core, icons, rte)')
  }
})

