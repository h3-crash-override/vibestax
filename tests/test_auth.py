from vibestax import detect


def _d(html="", headers=None, js_globals=None, url="", cookies=None):
    return detect(html=html, headers=headers or {}, js_globals=js_globals or [], url=url, cookies=cookies or {})


def test_clerk_script():
    r = _d(html='<script src="https://clerk.com/v1/clerk.browser.js"></script>')
    assert r.has("Clerk")


def test_auth0_js():
    r = _d(html='<script src="https://cdn.auth0.com/js/auth0-spa-js/2.0/auth0-spa-js.production.js"></script>')
    assert r.has("Auth0")


def test_auth0_url():
    r = _d(url="https://tenant.auth0.com/authorize?client_id=abc")
    assert r.has("Auth0")


def test_supabase_cookie():
    r = _d(cookies={"sb-us-east-1-auth-token": "eyJabc"})
    assert r.has("Supabase Auth")
    assert r.has("Supabase")  # implied


def test_okta_script():
    r = _d(html='<script src="https://ok.okta.com/js/okta-signin-widget/7.5.1/js/okta-sign-in.min.js"></script>')
    assert r.has("Okta")


def test_azure_ad_url():
    r = _d(url="https://login.microsoftonline.com/tenant/oauth2/v2.0/authorize")
    assert r.has("Azure AD")


def test_cognito_url():
    r = _d(url="https://cognito-idp.us-east-1.amazonaws.com/login")
    assert r.has("AWS Cognito")


def test_keycloak_realms():
    r = _d(url="https://auth.example.com/auth/realms/myrealm/protocol/openid-connect/auth")
    assert r.has("Keycloak")
