from .cms import RULES as _CMS
from .frameworks_js import RULES as _JS
from .frameworks_backend import RULES as _BACKEND
from .auth import RULES as _AUTH
from .hosting import RULES as _HOSTING
from .databases import RULES as _DB
from .ui_libraries import RULES as _UI
from .saas import RULES as _SAAS
from .portals import RULES as _PORTALS
from ..models import Rule

ALL_RULES: list[Rule] = [
    *_CMS,
    *_JS,
    *_BACKEND,
    *_AUTH,
    *_HOSTING,
    *_DB,
    *_UI,
    *_SAAS,
    *_PORTALS,
]
