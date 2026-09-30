from vibestax import detect


def _d(html="", headers=None, url=""):
    return detect(html=html, headers=headers or {}, url=url)


def test_vercel_header():
    r = _d(headers={"x-vercel-id": "iad1::abc123"})
    assert r.has("Vercel")


def test_vercel_url():
    r = _d(url="https://myapp.vercel.app")
    assert r.has("Vercel")


def test_netlify_header():
    r = _d(headers={"x-nf-request-id": "01abc"})
    assert r.has("Netlify")


def test_netlify_url():
    r = _d(url="https://myapp.netlify.app")
    assert r.has("Netlify")


def test_cloudflare_pages_url():
    r = _d(url="https://myapp.pages.dev")
    assert r.has("Cloudflare Pages")


def test_github_pages_url():
    r = _d(url="https://user.github.io/repo")
    assert r.has("GitHub Pages")


def test_railway_url():
    r = _d(url="https://myapp.up.railway.app")
    assert r.has("Railway")


def test_render_url():
    r = _d(url="https://myapp.onrender.com")
    assert r.has("Render")
