import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import Components from "unplugin-vue-components/vite";
import { AntDesignVueResolver } from "unplugin-vue-components/resolvers";
import { glob } from 'glob'
import path from 'path'
import { fileURLToPath, URL } from "url";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    Components({
      resolvers: [
        AntDesignVueResolver({
          importStyle: false, // css in js
        }),
      ],
    }),
  ],
  base: '/static/',
  root: './taskite/static',
  build: {
    manifest: 'manifest.json',
    rollupOptions: {
      input: glob.sync(path.resolve(__dirname, 'taskite/static/js/**/*.js'))
    }
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./taskite/static', import.meta.url))
    }
  }
});
