from vibestax import detect


def _d(html="", headers=None, url="", cookies=None, js_globals=None):
    return detect(html=html, headers=headers or {}, url=url, cookies=cookies or {}, js_globals=js_globals or [])


def test_salesforce_url():
    r = _d(url="https://myorg.salesforce.com")
    assert r.has("Salesforce")


def test_hubspot_cookie():
    r = _d(cookies={"hubspotutk": "abc123"})
    assert r.has("HubSpot")


def test_zendesk_url():
    r = _d(url="https://mycompany.zendesk.com")
    assert r.has("Zendesk")


def test_servicenow_url():
    r = _d(url="https://myco.service-now.com/nav_to.do")
    assert r.has("ServiceNow")


def test_shopify_cookie():
    r = _d(cookies={"_shopify_y": "abc", "cart_currency": "USD"})
    assert r.has("Shopify")


def test_intercom_script():
    r = _d(html='<script>window.intercomSettings = {app_id: "abc"}; Intercom("boot");</script>')
    assert r.has("Intercom")


def test_stripe_js():
    r = _d(html='<script src="https://js.stripe.com/v3/"></script>')
    assert r.has("Stripe")


def test_google_analytics():
    r = _d(html="<script>gtag('config', 'G-XXXXXXXXXX');</script>")
    assert r.has("Google Analytics")
