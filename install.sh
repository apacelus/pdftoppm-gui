#!/bin/bash
echo "Installing dependencies"
sudo apt install poppler-utils -y

echo "Verifying directories"
mkdir -p ~/.local/bin
mkdir -p ~/.local/share/applications/
mkdir -p ~/.local/share/icons/hicolor/512x512/apps/

echo "Downloading and extracting files"
curl -Lo ~/.local/bin/pdftoppm_gui "https://github.com/Apacelus/pdftoppm-gui/releases/download/latest/pdftoppm_gui.bin"
curl -o ~/.local/share/icons/hicolor/512x512/apps/pdftoppm_gui.png "https://raw.githubusercontent.com/Apacelus/pdftoppm-gui/main/logo.png"
curl -o ~/.local/share/applications/pdftoppm-gui.desktop "https://raw.githubusercontent.com/Apacelus/pdftoppm-gui/main/pdftoppm_gui.desktop"

echo "Updating permissions for executable"
chmod +x ~/.local/bin/pdftoppm_gui

echo "Updating icon cache"
gtk-update-icon-cache

echo "Installation is complete"
