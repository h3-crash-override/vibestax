from ..models import Rule, Signal, SignalSource as S

H = S.HTML
HD = S.HEADER
URL = S.URL

RULES: list[Rule] = [
    Rule(
        name="Vercel",
        category="Hosting",
        website="https://vercel.com",
        signals=[
            Signal(HD, r"x-vercel-id|x-vercel-cache|server.*vercel", confidence=100),
            Signal(HD, r"x-powered-by.*vercel", confidence=100),
            Signal(URL, r"\.vercel\.app", confidence=95),
        ],
    ),
    Rule(
        name="Netlify",
        category="Hosting",
        website="https://netlify.com",
        signals=[
            Signal(HD, r"x-nf-request-id|server.*netlify|netlify-vary", confidence=100),
            Signal(URL, r"\.netlify\.app|\.netlify\.com", confidence=95),
            Signal(H, r"netlify-identity|netlify\.com", confidence=80),
        ],
    ),
    Rule(
        name="Cloudflare Pages",
        category="Hosting",
        website="https://pages.cloudflare.com",
        signals=[
            Signal(HD, r"cf-ray|server.*cloudflare", confidence=90),
            Signal(URL, r"\.pages\.dev", confidence=95),
        ],
    ),
    Rule(
        name="Cloudflare Workers",
        category="Hosting",
        website="https://workers.cloudflare.com",
        signals=[
            Signal(HD, r"cf-ray|server.*cloudflare|cf-cache-status", confidence=80),
            Signal(URL, r"\.workers\.dev", confidence=95),
        ],
    ),
    Rule(
        name="AWS Amplify",
        category="Hosting",
        website="https://aws.amazon.com/amplify",
        signals=[
            Signal(H, r"@aws-amplify|aws-amplify", confidence=85),
            Signal(URL, r"amplifyapp\.com", confidence=100),
            Signal(HD, r"x-amz-cf-id|server.*AmazonS3", confidence=60),
        ],
    ),
    Rule(
        name="GitHub Pages",
        category="Hosting",
        website="https://pages.github.com",
        signals=[
            Signal(URL, r"\.github\.io", confidence=100),
            Signal(HD, r"server.*GitHub\.com", confidence=100),
        ],
    ),
    Rule(
        name="Railway",
        category="Hosting",
        website="https://railway.app",
        signals=[
            Signal(URL, r"\.railway\.app|up\.railway\.app", confidence=100),
            Signal(HD, r"x-railway|railway-environment", confidence=100),
        ],
    ),
    Rule(
        name="Render",
        category="Hosting",
        website="https://render.com",
        signals=[
            Signal(URL, r"\.onrender\.com", confidence=100),
        ],
    ),
    Rule(
        name="Fly.io",
        category="Hosting",
        website="https://fly.io",
        signals=[
            Signal(URL, r"\.fly\.dev|\.flycast\.dev", confidence=100),
            Signal(HD, r"fly-request-id", confidence=100),
        ],
    ),
]
