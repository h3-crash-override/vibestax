# vibestax

Apache 2.0 Python web technology fingerprinting — built for the age of AI-generated applications.

Every other Python fingerprinting library with meaningful adoption ([WAD](https://github.com/CERN-CERT/WAD), [python-Wappalyzer](https://github.com/chorsley/python-Wappalyzer), [webappanalyzer](https://github.com/enthec/webappanalyzer)) is GPL-3.0. vibestax is Apache 2.0, has zero required dependencies, and covers the modern stack — AI-scaffolded apps, edge-deployed SPAs, BaaS backends, and the auth/hosting layers that Wappalyzer doesn't track.

## Install

```bash
pip install vibestax

# With Playwright support (detect_from_page):
pip install "vibestax[playwright]"
```

## Usage

### From pre-fetched content

```python
from vibestax import detect

result = detect(
    url="https://example.com",
    html="...",                           # rendered HTML body
    headers={"x-powered-by": "Next.js"}, # HTTP response headers
    js_globals=["__NEXT_DATA__"],         # window.* globals (optional, requires browser)
)

result.detections          # list[Detection]
result.categories          # dict[str, list[Detection]]
result.has("Next.js")      # True
result.names()             # ["Next.js", "React"]
```

### With a live Playwright page

```python
from playwright.async_api import async_playwright
from vibestax import detect_from_page

async with async_playwright() as p:
    browser = await p.chromium.launch()
    page = await browser.new_page()
    await page.goto("https://example.com")

    result = await detect_from_page(page)
    print(result.categories)
```

## What it detects

| Category | Technologies |
|---|---|
| JS Frameworks | React, Next.js, Vue.js, Nuxt, Angular, SvelteKit, Svelte, Remix, Astro, Qwik, Solid, htmx, Alpine.js, Vite |
| CMS | WordPress, Drupal, Joomla, Ghost, Strapi, Contentful, Sanity, Payload CMS |
| Backend | FastAPI, Django, Ruby on Rails, Laravel, ASP.NET, Express.js, Spring Boot, Flask, Phoenix |
| Auth | Clerk, Auth0, Supabase Auth, Okta, Azure AD, AWS Cognito, Firebase Auth, Keycloak, OneLogin, PingIdentity |
| Hosting | Vercel, Netlify, Cloudflare Pages/Workers, AWS Amplify, GitHub Pages, Railway, Render, Fly.io |
| BaaS/DB | Supabase, Firebase, PlanetScale, Neon, Convex |
| UI Libraries | Tailwind CSS, shadcn/ui, Material UI, Chakra UI, Radix UI, Ant Design, Bootstrap |
| SaaS | Salesforce, HubSpot, Zendesk, ServiceNow, Shopify, Intercom, Workday, Jira, Confluence, Stripe, Datadog, Segment, Google Analytics |
| Network Portals | FortiGate, Pulse Secure, Palo Alto GlobalProtect, Cisco ASA, F5 BIG-IP, SonicWall, Juniper, Barracuda, Citrix (NetScaler + StoreFront), VMware Horizon, OWA, RDWeb, Zoho ManageEngine, Check Point |

## Detection result

```python
@dataclass
class Detection:
    name: str          # "Next.js"
    category: str      # "JS Framework"
    confidence: int    # 1–100
    implied: bool      # True if detected via implication, not direct signal
    website: str       # "https://nextjs.org"
```

## Rule authoring

Rules are Python dataclasses — no JSON, no external config, full IDE support:

```python
from vibestax.models import Rule, Signal, SignalSource as S

my_rule = Rule(
    name="MyApp Framework",
    category="JS Framework",
    website="https://myapp.dev",
    implies=["React"],           # auto-add "React" when this rule matches
    signals=[
        Signal(S.HTML,   r"myapp-root|__MYAPP_DATA__", confidence=90),
        Signal(S.HEADER, r"x-powered-by.*myapp",       confidence=100),
        Signal(S.JS_GLOBAL, r"MyApp\.",                confidence=95),
    ],
)
```

### Signal sources

| `SignalSource` | What it matches against |
|---|---|
| `HTML` | Rendered HTML body |
| `HEADER` | `header_name: value` lines (case-insensitive) |
| `META` | `<meta>` tag attribute strings |
| `COOKIE` | Cookie names and values |
| `JS_GLOBAL` | `window.*` global variable names (browser only) |
| `URL` | Final URL after redirects |

### Using a custom rule set

```python
from vibestax import detect
from vibestax.rules import ALL_RULES
from my_rules import MY_EXTRA_RULES

result = detect(url=url, html=html, rules=ALL_RULES + MY_EXTRA_RULES)
```

## License

Apache 2.0. See [LICENSE](LICENSE).

vibestax has zero required dependencies. The `playwright` extra adds `playwright>=1.40.0` (Apache 2.0).
