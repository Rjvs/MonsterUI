import type { Config } from 'tailwindcss'

export default {
  // MonsterUI applies classes dynamically via JS, so we need comprehensive content patterns
  // Combined with @source inline() patterns in styles.css for dynamic usage
  content: ["./index.html"],
  
  theme: {
    extend: {}
  },
  plugins: [],
} satisfies Config;