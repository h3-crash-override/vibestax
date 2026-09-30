from ..models import Rule, Signal, SignalSource as S

H = S.HTML
HD = S.HEADER
JS = S.JS_GLOBAL
MT = S.META
CK = S.COOKIE
URL = S.URL

RULES: list[Rule] = [
    Rule(
        name="WordPress",
        category="CMS",
        website="https://wordpress.org",
        signals=[
            Signal(H, r"/wp-content/", confidence=90),
            Signal(H, r"/wp-includes/", confidence=90),
            Signal(CK, r"wordpress_logged_in|wp-settings", confidence=95),
            Signal(HD, r"x-powered-by.*wp\b", confidence=80),
            Signal(MT, r'name=["\']generator["\'][^>]+WordPress', confidence=100),
        ],
    ),
    Rule(
        name="Drupal",
        category="CMS",
        website="https://drupal.org",
        signals=[
            Signal(H, r"/sites/default/files/", confidence=90),
            Signal(H, r'Drupal\.settings', confidence=95),
            Signal(CK, r"SESS[a-f0-9]+|Drupal\.visitor", confidence=85),
            Signal(MT, r'name=["\']generator["\'][^>]+Drupal', confidence=100),
            Signal(HD, r"x-generator.*drupal", confidence=100),
        ],
    ),
    Rule(
        name="Joomla",
        category="CMS",
        website="https://joomla.org",
        signals=[
            Signal(H, r"/media/jui/|/components/com_", confidence=90),
            Signal(MT, r'name=["\']generator["\'][^>]+Joomla', confidence=100),
            Signal(CK, r"joomla_user_state", confidence=95),
        ],
    ),
    Rule(
        name="Ghost",
        category="CMS",
        website="https://ghost.org",
        signals=[
            Signal(H, r'content=["\']Ghost \d', confidence=100),
            Signal(H, r"/ghost/api/|/content/images/", confidence=85),
            Signal(MT, r'name=["\']generator["\'][^>]+Ghost', confidence=100),
        ],
    ),
    Rule(
        name="Strapi",
        category="CMS",
        website="https://strapi.io",
        signals=[
            Signal(H, r"strapi", confidence=70),
            Signal(HD, r"x-powered-by.*strapi", confidence=100),
            Signal(URL, r"/api/strapi|strapi\.io", confidence=90),
        ],
    ),
    Rule(
        name="Contentful",
        category="CMS",
        website="https://contentful.com",
        signals=[
            Signal(H, r"cdn\.contentful\.com|images\.ctfassets\.net", confidence=95),
            Signal(JS, r"contentfulClient|window\.__contentful", confidence=100),
        ],
    ),
    Rule(
        name="Sanity",
        category="CMS",
        website="https://sanity.io",
        signals=[
            Signal(H, r"cdn\.sanity\.io", confidence=90),
            Signal(JS, r"__sanity|sanityClient", confidence=100),
        ],
    ),
    Rule(
        name="Payload CMS",
        category="CMS",
        website="https://payloadcms.com",
        signals=[
            Signal(H, r"/payload/|payload-cms", confidence=80),
            Signal(JS, r"window\.__PAYLOAD", confidence=100),
        ],
    ),
]
