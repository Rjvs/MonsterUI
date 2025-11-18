/* monsterui-icon-normalizer.js
 * Normalize all uk-icon / uk-spinner SVGs so UIKit/FrankenUI animations
 * always run in their canonical viewBox, and size is applied via transform.
 */

(function () {
  function normalizeUkIcon(icon) {
    const svg = icon.querySelector("svg");
    if (!svg) return;

    const viewBox = svg.viewBox && svg.viewBox.baseVal;
    if (!viewBox || !viewBox.width || !viewBox.height) return;

    const attrWidth = svg.width && svg.width.baseVal.value;
    const attrHeight = svg.height && svg.height.baseVal.value;

    // If no explicit attrs or they already match viewBox, nothing to do
    if (!attrWidth || !attrHeight) return;
    const scaleX = attrWidth / viewBox.width;
    const scaleY = attrHeight / viewBox.height;
    if (Math.abs(scaleX - 1) < 0.01 && Math.abs(scaleY - 1) < 0.01) return;

    // Use uniform scale based on X (UIKit spinners are square)
    const scale = scaleX;

    // Reset SVG back to canonical viewBox size
    svg.setAttribute("width", String(viewBox.width));
    svg.setAttribute("height", String(viewBox.height));

    // Apply scaling on the wrapper to preserve UIKit animations on <svg>
    const style = icon.style;
    if (!style.display) style.display = "inline-flex";
    style.alignItems = style.alignItems || "center";
    style.justifyContent = style.justifyContent || "center";
    style.transformOrigin = style.transformOrigin || "center";
    // Compose with any existing transform
    const existing = style.transform && style.transform !== "none"
      ? style.transform + " "
      : "";
    style.transform = existing + `scale(${scale})`;
  }

  function normalizeAllIcons(root) {
    root = root || document;
    root
      .querySelectorAll(".uk-icon, [uk-spinner], [data-uk-spinner]")
      .forEach(normalizeUkIcon);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      normalizeAllIcons(document);
    });
  } else {
    normalizeAllIcons(document);
  }

  // Optional: hook into UIkit/FrankenUI updates if they dynamically add icons.
  if (window.UIkit && typeof window.UIkit.on === "function") {
    window.UIkit.on("update", function (e) {
      if (e && e.target) normalizeAllIcons(e.target);
    });
  }
})();
