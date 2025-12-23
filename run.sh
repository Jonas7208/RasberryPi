#!/bin/bash
# Hybrid system: Python 3.13 for camera, Python 3.11 for CNN

set -e

# Capture image with Python 3.13 (system)
echo "📷 Capturing image..."
FILENAME=$(python3 capture.py | grep -oP 'still_.*\.jpg')

# Classify with Python 3.11 (venv)
echo "🤖 Classifying image..."
/home/jugendforscht26/py311env/bin/python classify.py "$FILENAME"
