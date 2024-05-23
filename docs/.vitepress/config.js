import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Taskite",
  description: "Open source Task Management Tool.",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Guide', link: '/introduction/home' },
      { text: 'Website', link: 'https://taskite.in' }
    ],

    sidebar: [
      // {
      //   text: 'Examples',
      //   items: [
      //     { text: 'Markdown Examples', link: '/markdown-examples' },
      //     { text: 'Runtime API Examples', link: '/api-examples' }
      //   ]
      // },
      {
        text: 'Getting Started',
        items: [
          {
            text: 'Home', link: '/introduction/home'
          }
        ]
      },
      {
        text: 'Self hosting',
        items: [
          {
            text: 'Overview', link: '/self-hosting/overview'
          }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/santoshkpatro/taskite' }
    ]
  }
})
