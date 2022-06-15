import adapter from '@sveltejs/adapter-static';

const config = {
	kit: {
		adapter: adapter({
			pages: 'build',
			assets: 'build',
			fallback: null,
			precompress: false
		}),
		prerender: { default: true },
		vite: {
			server: {
				fs: { allow: ['./static/'] }
			}
		}
	},
	experimental: {
		useVitePreprocess: true
	}
};

export default config;
