"""
Demo: Vite-Built Assets vs CDN Assets
===================================

This example demonstrates the difference between using CDN assets vs the new Vite-built assets.
The built assets combine Tailwind 4, FrankenUI 2.1.1, and DaisyUI 5 into a single optimized bundle.
"""

from fasthtml.common import *
from monsterui.all import *

# Example 1: Using the new Vite-built assets (recommended for production)
app_built = FastHTML(
    hdrs=Theme.blue.built_headers(icons=True, rte=True),  # 🆕 New Vite-built assets with icons & RTE
    title="MonsterUI with Vite-Built Assets"
)

# Example 2: Using traditional CDN assets (still available)
app_cdn = FastHTML(
    hdrs=Theme.blue.headers(),  # Traditional CDN assets
    title="MonsterUI with CDN Assets"
)

# Example 3: Using local downloaded assets
app_local = FastHTML(
    hdrs=Theme.blue.local_headers(),  # Downloads and serves locally
    title="MonsterUI with Local Assets"
)

@app_built.route("/")
def home():
    return Container(
        H1("MonsterUI with Vite-Built Assets", cls="text-3xl font-bold mb-6"),
        
        Alert(
            Div(
                H4("🚀 You're using Vite-built assets!", cls="alert-title"),
                P("This page loads:", cls="mb-2"),
                Ul(
                    Li("✅ Tailwind CSS 4 (with preflight/reset)"),
                    Li("✅ FrankenUI 2.1.1 (layered, no conflicts)"),
                    Li("✅ DaisyUI 5 (base reset disabled)"),
                    Li("✅ FrankenUI Icons (383KB, optional)"),
                    Li("✅ FrankenUI Rich Text Editor (343KB, optional)"),
                    cls="list-disc list-inside text-sm"
                ),
                P("CSS: 258KB + modular JS components from single version source!", cls="mt-2 font-semibold")
            ),
            type="info", cls="mb-6"
        ),
        
        H2("Component Compatibility Test", cls="text-2xl font-semibold mb-4"),
        
        Div(
            # Tailwind utilities
            Card(
                CardHeader(H3("Tailwind CSS 4", cls="card-title")),
                CardBody(
                    P("Utility classes: ", cls="mb-2"),
                    Div(
                        Span("text-blue-500", cls="bg-blue-100 text-blue-500 px-2 py-1 rounded mr-2"),
                        Span("bg-gradient-to-r", cls="bg-gradient-to-r from-purple-500 to-pink-500 text-white px-2 py-1 rounded mr-2"),
                        Span("shadow-lg", cls="bg-white shadow-lg px-2 py-1 rounded mr-2"),
                    ),
                    P("Grid layout:", cls="mt-4 mb-2"),
                    Div(
                        Div("Item 1", cls="bg-gray-200 p-2 rounded text-center"),
                        Div("Item 2", cls="bg-gray-200 p-2 rounded text-center"),
                        Div("Item 3", cls="bg-gray-200 p-2 rounded text-center"),
                        cls="grid grid-cols-3 gap-2"
                    )
                ),
                cls="mb-4"
            ),
            
            # DaisyUI components
            Card(
                CardHeader(H3("DaisyUI 5 Components", cls="card-title")),
                CardBody(
                    Div(
                        Button("Primary", cls="btn btn-primary mr-2"),
                        Button("Secondary", cls="btn btn-secondary mr-2"),
                        Button("Accent", cls="btn btn-accent mr-2"),
                        cls="mb-4"
                    ),
                    Div(
                        Div(
                            "Success Alert",
                            cls="alert alert-success"
                        ),
                        cls="mb-4"
                    ),
                    Div(
                        Input(type="text", placeholder="DaisyUI Input", cls="input input-bordered mr-2"),
                        Select(
                            Option("Option 1"),
                            Option("Option 2"),
                            Option("Option 3"),
                            cls="select select-bordered"
                        ),
                        cls="flex gap-2"
                    )
                ),
                cls="mb-4"
            ),
            
            # FrankenUI components
            Card(
                CardHeader(H3("FrankenUI 2.1.1 Components", cls="card-title")),
                CardBody(
                    P("UIkit-powered components:", cls="mb-3"),
                    Div(
                        Button("UK Button", cls="uk-button uk-button-default uk-margin-small-right"),
                        Button("UK Primary", cls="uk-button uk-button-primary uk-margin-small-right"),
                        Button("UK Secondary", cls="uk-button uk-button-secondary"),
                        cls="mb-4"
                    ),
                    Div(
                        Div(
                            H4("FrankenUI Card", cls="uk-card-title"),
                            P("This demonstrates FrankenUI's card component with UIkit styling."),
                            cls="uk-card-body"
                        ),
                        cls="uk-card uk-card-default uk-card-hover"
                    )
                ),
                cls="mb-4"
            ),
            
            cls="space-y-4"
        ),
        
        Details(
            Summary("🔧 Technical Details", cls="font-semibold cursor-pointer"),
            Div(
                H3("Asset Loading Comparison", cls="text-lg font-semibold mt-4 mb-2"),
                Table(
                    THead(
                        Tr(
                            Th("Method"),
                            Th("Files"),
                            Th("Size"),
                            Th("Conflicts"),
                            Th("Cache"),
                        )
                    ),
                    TBody(
                        Tr(
                            Td(Code("Theme.built_headers()")),
                            Td("1 CSS + 1-4 JS"),
                            Td("258KB CSS + modular JS"),
                            Td("✅ None"),
                            Td("✅ Long-term"),
                        ),
                        Tr(
                            Td(Code("Theme.headers()")),
                            Td("3 CSS + 3 JS"),
                            Td("~400KB total"),
                            Td("⚠️ Possible"),
                            Td("✅ CDN"),
                        ),
                        Tr(
                            Td(Code("Theme.local_headers()")),
                            Td("Downloaded files"),
                            Td("~400KB total"),
                            Td("⚠️ Possible"),
                            Td("✅ Local"),
                        ),
                    ),
                    cls="table table-zebra w-full"
                ),
                
                H3("Build Process", cls="text-lg font-semibold mt-6 mb-2"),
                Div(
                    Pre(
                        Code('''
# Install dependencies
cd vite && npm install

# Build optimized assets
npm run build

# Output: vite/outputs/monsterui.css
# - Tailwind 4 core + utilities
# - FrankenUI components (layered)  
# - DaisyUI components (no base conflicts)
''', cls="language-bash"),
                        cls="bg-base-200 p-4 rounded text-sm overflow-x-auto"
                    )
                ),
                cls="mt-4"
            ),
            cls="mt-6"
        ),
        
        cls="max-w-4xl mx-auto py-8"
    )

if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting Vite-Built Assets Demo")
    print("📦 Using Theme.blue.built_headers() for optimized asset loading")
    print("🌐 Open http://localhost:8000")
    uvicorn.run(app_built, host="0.0.0.0", port=8000)