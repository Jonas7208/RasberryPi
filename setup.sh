#!/bin/bash
# Automated setup script for RasberryPi trash recognition system

set -e

echo "🔧 RasberryPi Müll-Erkennungssystem - Setup"
echo "=========================================="
echo ""

# Check Python versions
echo "📋 Checking Python versions..."
python3 --version
if ! command -v python3.11 &> /dev/null; then
    echo "❌ Python 3.11 not found. Installing..."
    sudo apt update
    sudo apt install -y python3.11 python3.11-venv
else
    python3.11 --version
fi
echo ""

# Install system dependencies for camera
echo "📷 Installing camera dependencies..."
sudo apt install -y libcamera-dev python3-libcamera python3-picamera2
echo ""

# Create Python 3.11 virtual environment for TensorFlow Lite
echo "🐍 Creating Python 3.11 virtual environment..."
if [ ! -d "$HOME/py311env" ]; then
    python3.11 -m venv $HOME/py311env
fi
echo ""

# Install Python packages in venv
echo "📦 Installing TensorFlow Lite and dependencies..."
source $HOME/py311env/bin/activate
pip install --upgrade pip
pip install tflite-runtime numpy pillow
deactivate
echo ""

# Make scripts executable
echo "🔐 Making scripts executable..."
chmod +x capture.py classify.py run.sh
echo ""

# Test everything
echo "✅ Testing installation..."
echo ""

echo "Testing camera (Python 3.13)..."
python3 -c "from picamera2 import Picamera2; print('✓ picamera2 OK')"

echo "Testing TensorFlow Lite (Python 3.11)..."
$HOME/py311env/bin/python -c "import tflite_runtime.interpreter as tflite; print('✓ tflite OK')"

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Usage:"
echo "  ./run.sh              - Capture image and classify"
echo "  python3 capture.py    - Only capture image"
echo "  ~/py311env/bin/python classify.py <image> - Only classify"
