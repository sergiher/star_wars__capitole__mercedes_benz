import { reactRouter } from "@react-router/dev/vite";
import tailwindcss from "@tailwindcss/vite";
import { defineConfig } from "vite";
import tsconfigPaths from "vite-tsconfig-paths";

export default defineConfig({
  optimizeDeps: {
    include: ["react-toastify", "material-react-table", "@mui/material"],
  },
  plugins: [tailwindcss(), reactRouter(), tsconfigPaths()],
});
