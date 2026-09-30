from ..models import Rule, Signal, SignalSource as S

H = S.HTML
HD = S.HEADER
JS = S.JS_GLOBAL
MT = S.META
URL = S.URL

RULES: list[Rule] = [
    Rule(
        name="React",
        category="JS Framework",
        website="https://react.dev",
        signals=[
            Signal(H, r"data-reactroot|data-reactid|__reactFiber|__reactEvents", confidence=95),
            Signal(JS, r"React|__react_", confidence=80),
            Signal(H, r"react-dom", confidence=75),
        ],
    ),
    Rule(
        name="Next.js",
        category="JS Framework",
        website="https://nextjs.org",
        implies=["React"],
        signals=[
            Signal(H, r"/_next/static/", confidence=95),
            Signal(HD, r"x-powered-by.*next\.js", confidence=100),
            Signal(JS, r"__NEXT_DATA__|__next_f\s*=", confidence=100),
            Signal(H, r'id=["\']__NEXT_DATA__["\']', confidence=100),
        ],
    ),
    Rule(
        name="Vue.js",
        category="JS Framework",
        website="https://vuejs.org",
        signals=[
            Signal(H, r"data-v-[a-f0-9]+|__vue_app__|v-cloak", confidence=90),
            Signal(JS, r"Vue\.|__vue__", confidence=85),
            Signal(H, r'vue@\d|vue\.min\.js|vue\.runtime', confidence=90),
        ],
    ),
    Rule(
        name="Nuxt.js",
        category="JS Framework",
        website="https://nuxt.com",
        implies=["Vue.js"],
        signals=[
            Signal(H, r"/_nuxt/|__nuxt|nuxt-link", confidence=95),
            Signal(JS, r"__NUXT__|useNuxtApp", confidence=100),
            Signal(H, r'id=["\']__nuxt["\']', confidence=95),
        ],
    ),
    Rule(
        name="Angular",
        category="JS Framework",
        website="https://angular.dev",
        signals=[
            Signal(H, r"ng-version=|_nghost-|_ngcontent-", confidence=95),
            Signal(H, r"angular\.min\.js|@angular/core", confidence=90),
            Signal(JS, r"ng\.|angular\.", confidence=70),
        ],
    ),
    Rule(
        name="SvelteKit",
        category="JS Framework",
        website="https://kit.svelte.dev",
        implies=["Svelte"],
        signals=[
            Signal(H, r"/_app/|__sveltekit_", confidence=90),
            Signal(H, r'id=["\']svelte-announcer["\']', confidence=95),
            Signal(JS, r"__sveltekit|SvelteKit", confidence=100),
        ],
    ),
    Rule(
        name="Svelte",
        category="JS Framework",
        website="https://svelte.dev",
        signals=[
            Signal(H, r"svelte-\w{6,}|svelte\.js", confidence=80),
            Signal(JS, r"window\.__svelte", confidence=90),
        ],
    ),
    Rule(
        name="Remix",
        category="JS Framework",
        website="https://remix.run",
        implies=["React"],
        signals=[
            Signal(H, r'id=["\']__remix-error["\']|data-remix-', confidence=95),
            Signal(JS, r"__remixContext|RemixBrowser", confidence=100),
            Signal(H, r"@remix-run|remix\.run", confidence=85),
        ],
    ),
    Rule(
        name="Astro",
        category="JS Framework",
        website="https://astro.build",
        signals=[
            Signal(H, r"astro-island|data-astro-|astro:load", confidence=95),
            Signal(H, r"/_astro/", confidence=90),
        ],
    ),
    Rule(
        name="Qwik",
        category="JS Framework",
        website="https://qwik.dev",
        signals=[
            Signal(H, r"q:container|q:version=|qwik", confidence=95),
            Signal(JS, r"qwik\.|QwikCity", confidence=100),
        ],
    ),
    Rule(
        name="Solid.js",
        category="JS Framework",
        website="https://solidjs.com",
        signals=[
            Signal(H, r"solid-js|solidstart", confidence=80),
            Signal(JS, r"createSignal|createRoot|solid-js", confidence=85),
        ],
    ),
    Rule(
        name="Vite",
        category="Build Tool",
        website="https://vitejs.dev",
        signals=[
            Signal(H, r"/@vite/client|@vite/plugin|vite\.config", confidence=90),
            Signal(H, r'type=["\']module["\'][^>]+\.vite\.|vite-plugin', confidence=80),
        ],
    ),
    Rule(
        name="htmx",
        category="JS Framework",
        website="https://htmx.org",
        signals=[
            Signal(H, r"hx-get=|hx-post=|hx-swap=|htmx\.org", confidence=95),
        ],
    ),
    Rule(
        name="Alpine.js",
        category="JS Framework",
        website="https://alpinejs.dev",
        signals=[
            Signal(H, r"x-data=|x-show=|x-bind=|alpinejs", confidence=90),
        ],
    ),
]
