/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors: {
        "primary-dark": "#0C122D",
        "primary-light": "#F5F5F5",
        "accent-blue": "#4AB4CB",
        "boring-gray": "#9098BC",
      },
      fontFamily: {
        "fredoka": ["Fedroka One", "cursive"]
      },
      dropShadow: {
        "card": "0 3vh 3vh rgba(12, 18, 45, 0.25)",
        "card-huge": "0 0vh 50vh rgba(12, 18, 45, 0.75)",
      }
    },
  },
  plugins: [],
}
