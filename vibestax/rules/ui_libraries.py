from ..models import Rule, Signal, SignalSource as S

H = S.HTML
JS = S.JS_GLOBAL
URL = S.URL

RULES: list[Rule] = [
    Rule(
        name="Tailwind CSS",
        category="UI Library",
        website="https://tailwindcss.com",
        signals=[
            Signal(H, r'class="[^"]*\b(?:flex|grid|text-\w+|bg-\w+|p-\d|m-\d|rounded|shadow|border)[^"]*"', confidence=70),
            Signal(H, r"tailwindcss|cdn\.tailwindcss\.com", confidence=95),
            Signal(H, r"tw-\w+|@tailwind|tailwind\.config", confidence=85),
        ],
    ),
    Rule(
        name="shadcn/ui",
        category="UI Library",
        website="https://ui.shadcn.com",
        implies=["Tailwind CSS", "Radix UI"],
        signals=[
            Signal(H, r'class="[^"]*\b(?:cn\(|cva\(|shadcn)[^"]*"', confidence=75),
            Signal(H, r"@radix-ui.*tailwind|shadcn", confidence=90),
            Signal(H, r"cmdk|vaul|lucide-react", confidence=70),
        ],
    ),
    Rule(
        name="Material UI",
        category="UI Library",
        website="https://mui.com",
        signals=[
            Signal(H, r"@mui/|MuiButton|MuiBox|makeStyles", confidence=90),
            Signal(H, r"material-ui|Material-UI", confidence=85),
            Signal(JS, r"MUI|makeStyles\b", confidence=80),
        ],
    ),
    Rule(
        name="Chakra UI",
        category="UI Library",
        website="https://chakra-ui.com",
        signals=[
            Signal(H, r"@chakra-ui|chakra-ui|ChakraProvider", confidence=90),
            Signal(JS, r"ChakraProvider|useColorMode|chakra\.", confidence=90),
        ],
    ),
    Rule(
        name="Radix UI",
        category="UI Library",
        website="https://radix-ui.com",
        signals=[
            Signal(H, r"@radix-ui|radix-ui\.com|data-radix-", confidence=90),
        ],
    ),
    Rule(
        name="Bootstrap",
        category="UI Library",
        website="https://getbootstrap.com",
        signals=[
            Signal(H, r"bootstrap\.min\.css|bootstrap\.bundle|cdn\.jsdelivr\.net/npm/bootstrap", confidence=90),
            Signal(H, r'class="[^"]*\b(?:container|row|col-\w+|btn btn-|navbar)[^"]*"', confidence=65),
        ],
    ),
    Rule(
        name="Ant Design",
        category="UI Library",
        website="https://ant.design",
        signals=[
            Signal(H, r"ant-design|antd|@ant-design", confidence=90),
            Signal(H, r'class="[^"]*\bant-[a-z]+-[a-z]', confidence=85),
        ],
    ),
]
