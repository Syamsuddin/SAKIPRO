#!/bin/bash
echo "Building SAKIPRO v1.0 for macOS..."
pyinstaller --name sakipro main.py --noconfirm
echo "Build complete. Output is in dist/sakipro"
