"""Spinner Test Page - Debugging spinner implementations in MonsterUI"""

from fasthtml.common import *
from monsterui.all import *

# Use Vite-built assets (Tailwind 4 + FrankenUI 2.1.1 + DaisyUI 5)
app, rt = fast_app(hdrs=Theme.blue.built_headers())

@rt
def index():
    return Title("MonsterUI Spinner Test"), Container(
                    Div(
                        Div(uk_spinner="ratio: 0.5"),
                        Div(uk_spinner="ratio: 1.0"),
                        Div(uk_spinner="ratio: 1.5"),
                    ),
                )
# Test endpoint for HTMX
@rt("/test-endpoint")
def post():
    import time
    time.sleep(2)  # Simulate processing
    return "Done"

serve()
