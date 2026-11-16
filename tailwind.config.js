/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        rr: {
          pink: "#EA1D76",
          navy: "#10152B",
          midnight: "#080D1B",
          gold: "#D6B36A",
          offwhite: "#F5F4F7",
          surface: "#FFFFFF",
          card: "#FFFFFF",
          border: "#E5E7EB",
          borderSubtle: "#F3F4F6",
          muted: "#6B7280",
          textSecondary: "#4B5563",
          subtle: "#9CA3AF"
        }
      },
      fontFamily: {
        serif: ["Georgia", "Cambria", "Times New Roman", "serif"],
        sans: ["system-ui", "-apple-system", "BlinkMacSystemFont", "Segoe UI", "Roboto", "Helvetica Neue", "Arial", "sans-serif"],
        mono: ["ui-monospace", "SFMono-Regular", "Menlo", "Monaco", "Consolas", "monospace"],
      }
    },
  },
  plugins: [],
}
