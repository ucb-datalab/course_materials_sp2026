#!/bin/bash
# Setup script for AY128 course environment
set -e

echo "Setting up AY128 environment with uv..."

# Create virtual environment with Python 3.12
uv venv --python 3.12 --prompt ay128
source .venv/bin/activate

# Install all dependencies
echo "Installing dependencies..."
uv pip install -r requirements.txt

# Install Jupyter custom CSS for instant notebook styling
# Note: Jupyter only loads ~/.jupyter/custom/custom.css
# The source file is styles/ay128_custom.css for clarity
echo "Installing Jupyter custom CSS..."
JUPYTER_CUSTOM_DIR="$HOME/.jupyter/custom"
mkdir -p "$JUPYTER_CUSTOM_DIR"
cp styles/ay128_custom.css "$JUPYTER_CUSTOM_DIR/custom.css"

# Install IPython startup script for talktools module availability
echo "Installing IPython startup script..."
STARTUP_DIR="$HOME/.ipython/profile_default/startup"
mkdir -p "$STARTUP_DIR"
cp scripts/00-talktools-startup.py "$STARTUP_DIR/"

echo ""
echo "Setup complete!"
echo "To activate the environment, run: source .venv/bin/activate"
