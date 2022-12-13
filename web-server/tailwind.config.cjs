/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors: {
        "primary-dark": "#0C122D",
        "primary-light": "#F5F5F5"
      },
      fontFamily: {
        "fredoka": ["Fedroka One", "cursive"]
      }
    },
  },
  plugins: [],
}
