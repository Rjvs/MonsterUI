#!/usr/bin/env fish

# Visual testing script for MonsterUI examples
# Run each example, press Ctrl-C to stop and continue to next

source .venv/bin/activate.fish

# Handler to prevent script from exiting on Ctrl-C
# The Python process will still receive and handle the signal
function sigint_handler --on-signal SIGINT
    # Do nothing - let the Python process handle it
    return 0
end

for example in docs/examples/*.py
    echo ""
    echo "================================"
    echo "Testing: $example"
    echo "================================"
    echo ""
    echo "Visit http://localhost:5001 to inspect the UI"
    echo ""
    echo "Check:"
    echo "  - Layout and spacing"
    echo "  - Colors and themes"
    echo "  - Interactive elements"
    echo "  - Browser console for errors"
    echo "  - Network tab for CDN resources"
    echo ""
    echo "Press Ctrl-C to stop this example and continue to the next one"
    echo ""

    # Run the example in foreground - Ctrl-C will stop it but script continues
    python $example
    # Explicitly continue regardless of exit status (including SIGINT)
    true

    echo ""
    echo "→ Continuing to next example..."
    sleep 1
end

echo ""
echo "================================"
echo "Visual testing complete!"
echo "================================"
