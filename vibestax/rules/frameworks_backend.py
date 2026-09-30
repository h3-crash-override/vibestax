from ..models import Rule, Signal, SignalSource as S

H = S.HTML
HD = S.HEADER
JS = S.JS_GLOBAL
CK = S.COOKIE
URL = S.URL

RULES: list[Rule] = [
    Rule(
        name="FastAPI",
        category="Backend Framework",
        website="https://fastapi.tiangolo.com",
        signals=[
            Signal(H, r'"openapi":"3\.|FastAPI|fastapi"', confidence=80),
            Signal(HD, r"x-powered-by.*fastapi", confidence=100),
            Signal(H, r"/docs#/|/redoc|fastapi\.tiangolo", confidence=85),
        ],
    ),
    Rule(
        name="Django",
        category="Backend Framework",
        website="https://djangoproject.com",
        signals=[
            Signal(H, r"csrfmiddlewaretoken|django|__admin_media_prefix__", confidence=90),
            Signal(HD, r"x-frame-options.*DENY|x-frame-options.*SAMEORIGIN", confidence=40),
            Signal(H, r"</form>.*csrfmiddlewaretoken", confidence=95),
        ],
    ),
    Rule(
        name="Ruby on Rails",
        category="Backend Framework",
        website="https://rubyonrails.org",
        signals=[
            Signal(HD, r"x-powered-by.*Phusion Passenger|x-runtime.*\d\.\d+", confidence=80),
            Signal(H, r"csrf-token|rails-ujs|@rails/ujs", confidence=90),
            Signal(H, r'authenticity_token|name=["\']authenticity_token["\']', confidence=95),
        ],
    ),
    Rule(
        name="Laravel",
        category="Backend Framework",
        website="https://laravel.com",
        signals=[
            Signal(H, r"laravel|Illuminate\\|XSRF-TOKEN", confidence=80),
            Signal(H, r'csrf-token.*meta|meta.*csrf', confidence=75),
            Signal(HD, r"set-cookie.*XSRF-TOKEN|set-cookie.*laravel_session", confidence=95),
            Signal(CK, r"XSRF-TOKEN|laravel_session", confidence=95),
        ],
    ),
    Rule(
        name="ASP.NET",
        category="Backend Framework",
        website="https://asp.net",
        signals=[
            Signal(HD, r"x-powered-by.*ASP\.NET", confidence=100),
            Signal(HD, r"x-aspnet-version", confidence=100),
            Signal(H, r"__VIEWSTATE|__EVENTVALIDATION|WebResource\.axd", confidence=95),
            Signal(HD, r"server.*Microsoft-IIS", confidence=80),
        ],
    ),
    Rule(
        name="Express.js",
        category="Backend Framework",
        website="https://expressjs.com",
        signals=[
            Signal(HD, r"x-powered-by.*Express", confidence=100),
        ],
    ),
    Rule(
        name="Spring Boot",
        category="Backend Framework",
        website="https://spring.io",
        signals=[
            Signal(HD, r"x-application-context|x-content-type-options", confidence=40),
            Signal(H, r"org\.springframework|Spring Boot", confidence=90),
            Signal(URL, r"/actuator/health|/swagger-ui\.html|/v3/api-docs", confidence=85),
        ],
    ),
    Rule(
        name="Flask",
        category="Backend Framework",
        website="https://flask.palletsprojects.com",
        signals=[
            Signal(HD, r"server.*Werkzeug", confidence=95),
        ],
    ),
    Rule(
        name="Phoenix Framework",
        category="Backend Framework",
        website="https://phoenixframework.org",
        signals=[
            Signal(H, r"phx-|LiveView|phoenix\.js", confidence=90),
            Signal(HD, r"x-powered-by.*phoenix|server.*cowboy", confidence=85),
        ],
    ),
]
