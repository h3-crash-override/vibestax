from ..models import Rule, Signal, SignalSource as S

H = S.HTML
HD = S.HEADER
JS = S.JS_GLOBAL
CK = S.COOKIE
URL = S.URL

RULES: list[Rule] = [
    Rule(
        name="Salesforce",
        category="SaaS",
        website="https://salesforce.com",
        signals=[
            Signal(URL, r"\.salesforce\.com|\.force\.com|\.lightning\.force\.com", confidence=100),
            Signal(H, r"salesforce\.com|lightning-component|LCC\.", confidence=90),
            Signal(JS, r"sforce\.|Sfdc\.", confidence=95),
        ],
    ),
    Rule(
        name="HubSpot",
        category="SaaS",
        website="https://hubspot.com",
        signals=[
            Signal(H, r"hs-scripts\.com|hubspot\.com|hbspt\.", confidence=95),
            Signal(JS, r"hbspt\.|HubSpot\.", confidence=95),
            Signal(CK, r"hubspotutk|__hstc|__hssc", confidence=100),
        ],
    ),
    Rule(
        name="Zendesk",
        category="SaaS",
        website="https://zendesk.com",
        signals=[
            Signal(URL, r"\.zendesk\.com|\.zendeskcdn\.com", confidence=100),
            Signal(H, r"zendesk\.com|zendeskWidget|zE\(", confidence=90),
            Signal(JS, r"zE\b|zESettings|zendesk", confidence=90),
        ],
    ),
    Rule(
        name="ServiceNow",
        category="SaaS",
        website="https://servicenow.com",
        signals=[
            Signal(URL, r"\.service-now\.com|\.servicenow\.com", confidence=100),
            Signal(H, r"ServiceNow|service-now\.com", confidence=90),
        ],
    ),
    Rule(
        name="Shopify",
        category="SaaS",
        website="https://shopify.com",
        signals=[
            Signal(H, r"cdn\.shopify\.com|shopify\.com|Shopify\.theme", confidence=95),
            Signal(JS, r"Shopify\.|ShopifyAnalytics", confidence=95),
            Signal(CK, r"_shopify_y|_shopify_s|cart_currency", confidence=100),
        ],
    ),
    Rule(
        name="Intercom",
        category="SaaS",
        website="https://intercom.com",
        signals=[
            Signal(H, r"widget\.intercom\.io|Intercom\(|intercom\.io", confidence=95),
            Signal(JS, r"Intercom\b|window\.intercomSettings", confidence=100),
        ],
    ),
    Rule(
        name="Workday",
        category="SaaS",
        website="https://workday.com",
        signals=[
            Signal(URL, r"\.myworkday\.com|workday\.com", confidence=100),
            Signal(H, r"workday\.com|wd5\.myworkday", confidence=90),
        ],
    ),
    Rule(
        name="Confluence",
        category="SaaS",
        website="https://atlassian.com/confluence",
        implies=["Atlassian"],
        signals=[
            Signal(H, r"AJS\.params|confluence\.atlassian\.com|confluence-context", confidence=90),
            Signal(URL, r"\.confluence\.|/confluence/", confidence=85),
        ],
    ),
    Rule(
        name="Jira",
        category="SaaS",
        website="https://atlassian.com/jira",
        implies=["Atlassian"],
        signals=[
            Signal(H, r"jira\.atlassian\.com|atlassian\.com/jira|JIRA\.navigator", confidence=90),
            Signal(URL, r"\.atlassian\.net/jira|/jira/software/", confidence=95),
        ],
    ),
    Rule(
        name="Atlassian",
        category="SaaS",
        website="https://atlassian.com",
        signals=[
            Signal(URL, r"\.atlassian\.net|atlassian\.com", confidence=90),
            Signal(H, r"atlassian\.com|AJS\.", confidence=80),
        ],
    ),
    Rule(
        name="Stripe",
        category="SaaS",
        website="https://stripe.com",
        signals=[
            Signal(H, r"js\.stripe\.com|Stripe\(|stripe\.com", confidence=95),
            Signal(JS, r"Stripe\b|stripe\.elements", confidence=95),
        ],
    ),
    Rule(
        name="Datadog",
        category="SaaS",
        website="https://datadoghq.com",
        signals=[
            Signal(H, r"datadoghq\.com|datadog-rum|DD_RUM", confidence=95),
            Signal(JS, r"DD_RUM\.|window\.__DD_", confidence=100),
        ],
    ),
    Rule(
        name="Segment",
        category="SaaS",
        website="https://segment.com",
        signals=[
            Signal(H, r"cdn\.segment\.com|analytics\.js", confidence=85),
            Signal(JS, r"analytics\.identify|analytics\.track|window\.analytics", confidence=80),
        ],
    ),
    Rule(
        name="Google Analytics",
        category="Analytics",
        website="https://analytics.google.com",
        signals=[
            Signal(H, r"google-analytics\.com|googletagmanager\.com|gtag\(|GA_MEASUREMENT", confidence=90),
            Signal(JS, r"gtag\b|ga\(|_gaq\.push", confidence=85),
        ],
    ),
]
