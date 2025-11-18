
import { Window } from 'happy-dom';
import { readFileSync } from 'fs';

const html = readFileSync('tailwind_test.html', 'utf8');
const window = new Window({ url: 'http://localhost' });
const document = window.document;

// Parse and load HTML properly
document.documentElement.innerHTML = html;

// Make global objects available for Tailwind
global.window = window;
global.document = document;

// Execute the script tags
const scripts = document.querySelectorAll('script');
for (const script of scripts) {
    if (script.textContent) {
        try {
            eval(script.textContent);
        } catch (e) {
            console.error('Error executing script:', e.message);
        }
    }
}

// Wait for Tailwind to process
await new Promise(resolve => setTimeout(resolve, 3000));

const styleTag = document.querySelector('style');
if (styleTag) {
    console.log(styleTag.textContent);
} else {
    console.error('No style tag found');
    console.error('Head content:', document.head.innerHTML.slice(0, 500));
    process.exit(1);
}

process.exit(0);
