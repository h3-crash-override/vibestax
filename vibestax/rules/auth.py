from ..models import Rule, Signal, SignalSource as S

H = S.HTML
HD = S.HEADER
JS = S.JS_GLOBAL
CK = S.COOKIE
URL = S.URL

RULES: list[Rule] = [
    Rule(
        name="Clerk",
        category="Auth Provider",
        website="https://clerk.com",
        signals=[
            Signal(H, r"clerk\.com|@clerk/|frontend-api\.clerk\.com", confidence=95),
            Signal(JS, r"Clerk\.|__clerk_", confidence=100),
            Signal(H, r"clerk-js", confidence=90),
        ],
    ),
    Rule(
        name="Auth0",
        category="Auth Provider",
        website="https://auth0.com",
        signals=[
            Signal(H, r"auth0\.com|cdn\.auth0\.com|@auth0/", confidence=95),
            Signal(JS, r"Auth0Client|createAuth0Client|window\.auth0", confidence=100),
            Signal(URL, r"\.auth0\.com|auth0\.com/authorize", confidence=100),
        ],
    ),
    Rule(
        name="Supabase Auth",
        category="Auth Provider",
        website="https://supabase.com",
        implies=["Supabase"],
        signals=[
            Signal(H, r"supabase\.co|@supabase/auth|supabase-js", confidence=90),
            Signal(JS, r"supabase\.auth\.|createClient.*supabase", confidence=95),
            Signal(CK, r"sb-[\w-]+-auth-token", confidence=100),
        ],
    ),
    Rule(
        name="Okta",
        category="Auth Provider",
        website="https://okta.com",
        signals=[
            Signal(H, r"okta\.com|@okta/|okta-signin-widget", confidence=95),
            Signal(JS, r"OktaAuth|OktaSignIn", confidence=100),
            Signal(URL, r"\.okta\.com|okta\.com/oauth2", confidence=100),
        ],
    ),
    Rule(
        name="Azure AD",
        category="Auth Provider",
        website="https://azure.microsoft.com",
        signals=[
            Signal(URL, r"login\.microsoftonline\.com|login\.live\.com", confidence=100),
            Signal(H, r"@azure/msal|msal\.js|msal-browser", confidence=95),
            Signal(JS, r"PublicClientApplication|msalInstance|msal\.", confidence=90),
        ],
    ),
    Rule(
        name="AWS Cognito",
        category="Auth Provider",
        website="https://aws.amazon.com/cognito",
        signals=[
            Signal(H, r"cognito-idp\.|amazonaws\.com/cognito|@aws-amplify/auth", confidence=95),
            Signal(JS, r"CognitoUserPool|Auth\.signIn|aws-amplify/auth", confidence=90),
            Signal(URL, r"cognito-idp\.[\w-]+\.amazonaws\.com", confidence=100),
        ],
    ),
    Rule(
        name="Firebase Auth",
        category="Auth Provider",
        website="https://firebase.google.com",
        implies=["Firebase"],
        signals=[
            Signal(H, r"firebase/auth|firebaseapp\.com", confidence=90),
            Signal(JS, r"getAuth|signInWithEmailAndPassword|firebase\.auth", confidence=90),
        ],
    ),
    Rule(
        name="Keycloak",
        category="Auth Provider",
        website="https://keycloak.org",
        signals=[
            Signal(H, r"keycloak\.js|keycloak-js|/auth/realms/", confidence=95),
            Signal(JS, r"Keycloak\(|keycloak\.init", confidence=100),
            Signal(URL, r"/auth/realms/|/realms/[^/]+/protocol/openid", confidence=100),
        ],
    ),
    Rule(
        name="OneLogin",
        category="Auth Provider",
        website="https://onelogin.com",
        signals=[
            Signal(URL, r"\.onelogin\.com", confidence=100),
            Signal(H, r"onelogin", confidence=80),
        ],
    ),
    Rule(
        name="PingIdentity",
        category="Auth Provider",
        website="https://pingidentity.com",
        signals=[
            Signal(URL, r"pingfederate|pingone\.com|\.ping\.com", confidence=95),
            Signal(H, r"pingfederate|PingFederate", confidence=90),
        ],
    ),
]
