"""High-value external-facing portals — VPNs, remote access gateways, enterprise infra.

These rules complement favicon hash detection in web-recon. HTML/header signals here
catch portals where the favicon isn't fetched or the hash table isn't populated.
"""
from ..models import Rule, Signal, SignalSource as S

H = S.HTML
HD = S.HEADER
URL = S.URL

RULES: list[Rule] = [
    Rule(
        name="Fortinet FortiGate VPN",
        category="Network Portal",
        website="https://fortinet.com",
        signals=[
            Signal(H, r"FortiGate|FortiNet|fgt_lang|SSL VPN.*Fortinet", confidence=95),
            Signal(H, r"/remote/login|/remote/hostcheck_validate", confidence=85),
            Signal(HD, r"fortinet|fortigate", confidence=90),
        ],
    ),
    Rule(
        name="Pulse Secure VPN",
        category="Network Portal",
        website="https://pulsesecure.net",
        signals=[
            Signal(H, r"Pulse Secure|PulseSecure|/dana-na/|/dana/html5", confidence=95),
            Signal(H, r"welcome to the Juniper SSL VPN|dana-cached", confidence=90),
        ],
    ),
    Rule(
        name="Palo Alto GlobalProtect",
        category="Network Portal",
        website="https://paloaltonetworks.com",
        signals=[
            Signal(H, r"GlobalProtect|/global-protect/|gp-login", confidence=95),
            Signal(H, r"Palo Alto Networks.*VPN|PAN-OS", confidence=90),
        ],
    ),
    Rule(
        name="Cisco ASA WebVPN",
        category="Network Portal",
        website="https://cisco.com",
        signals=[
            Signal(H, r"Cisco.*AnyConnect|Cisco.*SSL VPN", confidence=90),
            Signal(H, r"webvpn|WEBVPN_COOKIE", confidence=90),
            Signal(URL, r"CSCOE|CSCOU", confidence=95),
        ],
    ),
    Rule(
        name="F5 BIG-IP APM",
        category="Network Portal",
        website="https://f5.com",
        signals=[
            Signal(H, r"BIG-IP|F5 Networks|/my\.policy|MRHSession", confidence=90),
            Signal(HD, r"server.*BigIP|set-cookie.*MRHSession", confidence=95),
        ],
    ),
    Rule(
        name="SonicWall SSL-VPN",
        category="Network Portal",
        website="https://sonicwall.com",
        signals=[
            Signal(H, r"SonicWall|SonicOS|NetExtender|/cgi-bin/welcome/", confidence=90),
        ],
    ),
    Rule(
        name="Juniper SSL VPN",
        category="Network Portal",
        website="https://juniper.net",
        signals=[
            Signal(H, r"Juniper Networks.*SSL VPN|juniper.*secure|/dana-na/", confidence=90),
        ],
    ),
    Rule(
        name="Barracuda SSL VPN",
        category="Network Portal",
        website="https://barracuda.com",
        signals=[
            Signal(H, r"Barracuda.*VPN|barracuda.*ssl|BarracudaVPN", confidence=90),
        ],
    ),
    Rule(
        name="Citrix NetScaler",
        category="Network Portal",
        website="https://citrix.com",
        signals=[
            Signal(H, r"Citrix.*Gateway|NetScaler|/vpn/index\.html|ns_af=", confidence=90),
            Signal(HD, r"citrix-transactionid|x-citrix", confidence=95),
            Signal(URL, r"/vpn/index\.html", confidence=80),
        ],
    ),
    Rule(
        name="Citrix StoreFront",
        category="Network Portal",
        website="https://citrix.com",
        signals=[
            Signal(H, r"StoreFront|Citrix.*Receiver|/Citrix/Store|ctxsf", confidence=90),
        ],
    ),
    Rule(
        name="VMware Horizon",
        category="Network Portal",
        website="https://vmware.com",
        signals=[
            Signal(H, r"VMware Horizon|horizon\.vmware\.com|/portal/webclient", confidence=90),
            Signal(H, r"View Portal|VMWARE.*Horizon", confidence=85),
        ],
    ),
    Rule(
        name="Microsoft OWA",
        category="Network Portal",
        website="https://microsoft.com",
        signals=[
            Signal(H, r"Outlook Web App|OWA|/owa/|Exchange.*Outlook", confidence=90),
            Signal(H, r"OutlookSession|X-OWA-Version", confidence=85),
            Signal(HD, r"x-owa-version|x-feserver", confidence=95),
        ],
    ),
    Rule(
        name="Microsoft RDWeb",
        category="Network Portal",
        website="https://microsoft.com",
        signals=[
            Signal(H, r"Remote Desktop Web Access|RDWeb|RD Web|/rdweb/", confidence=95),
        ],
    ),
    Rule(
        name="Zoho ManageEngine",
        category="Network Portal",
        website="https://manageengine.com",
        signals=[
            Signal(H, r"ManageEngine|ZOHO.*ManageEngine|ADSelfService|ServiceDesk Plus", confidence=90),
            Signal(HD, r"x-zoho|manageengine", confidence=85),
        ],
    ),
    Rule(
        name="Check Point SSL VPN",
        category="Network Portal",
        website="https://checkpoint.com",
        signals=[
            Signal(H, r"Check Point|SSL Network Extender|/sslvpn/|cpLGN", confidence=90),
        ],
    ),
]
