from vibestax import detect


def _d(html="", headers=None, url=""):
    return detect(html=html, headers=headers or {}, url=url)


def test_aspnet_header():
    r = _d(headers={"x-powered-by": "ASP.NET"})
    assert r.has("ASP.NET")


def test_aspnet_version_header():
    r = _d(headers={"x-aspnet-version": "4.0.30319"})
    assert r.has("ASP.NET")


def test_aspnet_viewstate():
    r = _d(html='<input type="hidden" name="__VIEWSTATE" value="abc">')
    assert r.has("ASP.NET")


def test_express_header():
    r = _d(headers={"x-powered-by": "Express"})
    assert r.has("Express.js")


def test_flask_werkzeug():
    r = _d(headers={"server": "Werkzeug/3.0"})
    assert r.has("Flask")


def test_django_csrf():
    r = _d(html='<input type="hidden" name="csrfmiddlewaretoken" value="abc">')
    assert r.has("Django")


def test_rails_authenticity_token():
    r = _d(html='<input name="authenticity_token" value="abc">')
    assert r.has("Ruby on Rails")


def test_laravel_cookie(monkeypatch):
    r = detect(headers={}, cookies={"XSRF-TOKEN": "abc", "laravel_session": "xyz"})
    assert r.has("Laravel")


def test_spring_actuator_url():
    r = _d(url="https://api.example.com/actuator/health")
    assert r.has("Spring Boot")
