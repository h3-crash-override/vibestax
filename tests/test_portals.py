from vibestax import detect


def _d(html="", headers=None, url=""):
    return detect(html=html, headers=headers or {}, url=url)


def test_fortigate():
    r = _d(html="<title>FortiGate SSL VPN</title><a href='/remote/login'>Login</a>")
    assert r.has("Fortinet FortiGate VPN")


def test_pulse_secure():
    r = _d(html="<title>Pulse Secure</title><script src='/dana-na/auth/url_default/welcome.cgi'></script>")
    assert r.has("Pulse Secure VPN")


def test_globalprotect():
    r = _d(html="<title>GlobalProtect Portal</title>")
    assert r.has("Palo Alto GlobalProtect")


def test_cisco_asa():
    r = _d(url="https://vpn.example.com/+CSCOE+/logon.html")
    assert r.has("Cisco ASA WebVPN")


def test_f5_bigip_cookie():
    r = _d(headers={"set-cookie": "MRHSession=abc; path=/; secure"})
    assert r.has("F5 BIG-IP APM")


def test_owa():
    r = _d(html="<title>Outlook Web App</title>", headers={"x-owa-version": "15.2"})
    assert r.has("Microsoft OWA")


def test_rdweb():
    r = _d(html="<title>Remote Desktop Web Access</title>")
    assert r.has("Microsoft RDWeb")


def test_citrix_netscaler_path():
    r = _d(url="https://access.example.com/vpn/index.html")
    assert r.has("Citrix NetScaler")


def test_vmware_horizon():
    r = _d(html="<title>VMware Horizon</title>")
    assert r.has("VMware Horizon")
