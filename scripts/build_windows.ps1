Write-Host "Building SAKIPRO v1.0 for Windows..."
pyinstaller --name sakipro main.py --noconfirm
Write-Host "Build complete. Output is in dist\sakipro"
