from vibestax import detect


def _d(html="", headers=None, url=""):
    return detect(html=html, headers=headers or {}, url=url)


def test_wordpress_wp_content():
    r = _d(html='<link rel="stylesheet" href="/wp-content/themes/main.css">')
    assert r.has("WordPress")


def test_wordpress_meta_generator():
    r = _d(html='<meta name="generator" content="WordPress 6.4">')
    assert r.has("WordPress")


def test_drupal_settings():
    r = _d(html="<script>Drupal.settings = {};</script>")
    assert r.has("Drupal")


def test_joomla_generator():
    r = _d(html='<meta name="generator" content="Joomla! 4.0">')
    assert r.has("Joomla")


def test_ghost_meta():
    r = _d(html='<meta name="generator" content="Ghost 5.0">')
    assert r.has("Ghost")


def test_strapi_header():
    r = _d(headers={"x-powered-by": "Strapi"})
    assert r.has("Strapi")


def test_contentful_cdn():
    r = _d(html='<img src="https://images.ctfassets.net/abc/image.png">')
    assert r.has("Contentful")
