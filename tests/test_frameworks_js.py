from vibestax import detect


def _d(html="", headers=None, js_globals=None, url=""):
    return detect(html=html, headers=headers or {}, js_globals=js_globals or [], url=url)


def test_nextjs_static_path():
    r = _d(html='<script src="/_next/static/chunks/main.js"></script>')
    assert r.has("Next.js")
    assert r.has("React")  # implied


def test_nextjs_header():
    r = _d(headers={"x-powered-by": "Next.js 14.0"})
    assert r.has("Next.js")


def test_react_fiber():
    r = _d(html='<div data-reactroot __reactFiber123="x"></div>')
    assert r.has("React")


def test_vue_data_attr():
    r = _d(html='<div data-v-1a2b3c4d></div>')
    assert r.has("Vue.js")


def test_nuxt_path():
    r = _d(html='<script src="/_nuxt/entry.js"></script><div id="__nuxt"></div>')
    assert r.has("Nuxt.js")
    assert r.has("Vue.js")  # implied


def test_sveltekit_app_path():
    r = _d(html='<script src="/_app/immutable/entry.js"></script>')
    assert r.has("SvelteKit")


def test_angular_ng_version():
    r = _d(html='<app-root ng-version="17.0.0"></app-root>')
    assert r.has("Angular")


def test_remix_context():
    r = _d(js_globals=["__remixContext", "React"])
    assert r.has("Remix")


def test_astro_island():
    r = _d(html="<astro-island uid='abc'></astro-island>")
    assert r.has("Astro")


def test_htmx():
    r = _d(html='<button hx-get="/api/data" hx-swap="outerHTML">Load</button>')
    assert r.has("htmx")
