#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Adjust this if your path is different:
const CSS_PATH = path.resolve(
  __dirname,
  "../node_modules/franken-ui/dist/franken-ui.css"
);

const css = fs.readFileSync(CSS_PATH, "utf8");

// .uk-theme-emerald { ... }
const lightRe = /\.uk-theme-([a-z0-9-]+)\s*\{([^}]+)\}/gi;
// .dark.uk-theme-emerald { ... }
const darkRe = /\.dark\.uk-theme-([a-z0-9-]+)\s*\{([^}]+)\}/gi;

const parseBlock = (block) => {
  const vars = {};
  const varRe = /(--[a-z0-9-]+)\s*:\s*([^;]+);/gi;
  let m;
  while ((m = varRe.exec(block))) {
    vars[m[1]] = m[2].trim();
  }
  return vars;
};

const themes = {};

let m;
while ((m = lightRe.exec(css))) {
  const [, name, body] = m;
  themes[name] ??= {};
  themes[name].light = parseBlock(body);
}

while ((m = darkRe.exec(css))) {
  const [, name, body] = m;
  themes[name] ??= {};
  themes[name].dark = parseBlock(body);
}

const outJson = path.resolve(__dirname, "franken-themes.json");
fs.writeFileSync(outJson, JSON.stringify(themes, null, 2), "utf8");

const outCsv = path.resolve(__dirname, "franken-themes.csv");
const lines = [
  "theme,mode,token,value",
  ...Object.entries(themes).flatMap(([theme, modes]) =>
    ["light", "dark"].flatMap((mode) => {
      if (!modes[mode]) return [];
      return Object.entries(modes[mode]).map(
        ([token, value]) => `${theme},${mode},${token},"${value}"`
      );
    })
  ),
];

fs.writeFileSync(outCsv, lines.join("\n"), "utf8");

console.log(`Wrote ${outJson}`);
console.log(`Wrote ${outCsv}`);
