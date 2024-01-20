/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: "#00A878", // Green
          100: "#E6F8F2",
          200: "#B3ECD9",
          300: "#80E0BF",
          400: "#4DD4A6",
          500: "#00A878", // Same as DEFAULT
          600: "#008262",
          700: "#00604D",
          800: "#004037",
          900: "#002022",
        },
        accent: {
          DEFAULT: "#FFB400", // Orange
          100: "#FFF4D8",
          200: "#FFEAAB",
          300: "#FFDF7E",
          400: "#FFD551",
          500: "#FFB400", // Same as DEFAULT
          600: "#E69C00",
          700: "#B37A00",
          800: "#805800",
          900: "#4D3700",
        },
        background: {
          DEFAULT: "#FFFFFF", // White
          100: "#FFFFFF",
          200: "#F2F2F2",
          300: "#E6E6E6",
          400: "#D9D9D9",
          500: "#CCCCCC",
          600: "#BFBFBF",
          700: "#B3B3B3",
          800: "#A6A6A6",
          900: "#999999",
        },
      },
    },
  },
  plugins: [],
};
