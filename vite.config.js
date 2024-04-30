import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import Components from 'unplugin-vue-components/vite'
import { AntDesignVueResolver } from 'unplugin-vue-components/resolvers'
import ckeditor5 from '@ckeditor/vite-plugin-ckeditor5'
import { createRequire } from 'node:module';
const require = createRequire( import.meta.url );
import { glob } from 'glob'
import path from 'path'
import { fileURLToPath, URL } from 'url'

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
    ckeditor5( { theme: require.resolve( '@ckeditor/ckeditor5-theme-lark' ) } )
  ],
  base: '/static/',
  root: './taskite/static',
  build: {
    manifest: 'manifest.json',
    rollupOptions: {
      input: glob.sync(path.resolve(__dirname, 'taskite/static/entrypoints/**/*.js')),
    },
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./taskite/static', import.meta.url)),
    },
  },
})
