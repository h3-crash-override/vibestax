from ..models import Rule, Signal, SignalSource as S

H = S.HTML
HD = S.HEADER
JS = S.JS_GLOBAL
URL = S.URL

RULES: list[Rule] = [
    Rule(
        name="Supabase",
        category="BaaS",
        website="https://supabase.com",
        signals=[
            Signal(H, r"supabase\.co|@supabase/supabase-js|supabase-js", confidence=90),
            Signal(JS, r"createClient.*supabase|supabase\.from\(", confidence=95),
            Signal(URL, r"\.supabase\.co", confidence=100),
        ],
    ),
    Rule(
        name="Firebase",
        category="BaaS",
        website="https://firebase.google.com",
        signals=[
            Signal(H, r"firebaseapp\.com|firebase\.google\.com|@firebase/", confidence=90),
            Signal(JS, r"firebase\.initializeApp|getFirestore|getDatabase\b", confidence=90),
            Signal(URL, r"\.firebaseapp\.com|\.firebase\.google\.com", confidence=100),
        ],
    ),
    Rule(
        name="PlanetScale",
        category="Database",
        website="https://planetscale.com",
        signals=[
            Signal(H, r"@planetscale|planetscale", confidence=85),
            Signal(URL, r"\.planetscale\.com", confidence=100),
        ],
    ),
    Rule(
        name="Neon",
        category="Database",
        website="https://neon.tech",
        signals=[
            Signal(H, r"@neondatabase|neon\.tech", confidence=85),
            Signal(URL, r"\.neon\.tech|neondb\.io", confidence=100),
        ],
    ),
    Rule(
        name="Convex",
        category="BaaS",
        website="https://convex.dev",
        signals=[
            Signal(H, r"convex\.dev|@convex-dev/react", confidence=90),
            Signal(JS, r"ConvexProvider|useConvex\b", confidence=95),
        ],
    ),
]
