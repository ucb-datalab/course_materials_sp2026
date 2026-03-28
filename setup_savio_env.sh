#!/bin/bash
# Setup script for AY128 course environment on Savio
set -e

module load gcc python proj ml/pytorch

echo "Setting up AY128 environment with uv..."

echo "Downloading uv"
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment with Python 3.12
uv venv -v --python 3.11 --prompt ay128
source .venv/bin/activate

# Install all dependencies
echo "Installing dependencies..."
uv pip install -r requirements.txt

python -m ipykernel install --user --name=ay128 --display-name "Python (AY128)"

echo "Setup complete!"
echo "To activate the environment, run: source .venv/bin/activate"
