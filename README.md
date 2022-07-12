# pdftoppm-gui
GUI tool for converting pdfs to images. Uses the pdftoppm cli tool.
## Installation
Run this command **without** sudo: ```curl https://raw.githubusercontent.com/Apacelus/pdftoppm-gui/main/install.sh | bash```
## Build instructions
These are the manual install instructions. If you wish to quickly install, use the command from [Installation](https://github.com/Apacelus/pdftoppm-gui#installation)
1. Clone repo: ```git clone "https://github.com/Apacelus/pdftoppm-gui.git" && cd pdftoppm-gui```
2. Install Nuitka: ```pip install Nuitka```
3. Compile binary: ```python3 -m nuitka main.py```
4. Place compiled binary in ```~/.local/bin/```
5. Make binary executable: ```chmod +x ~/local/bin/<binary-name>```
6. Place pdftoppm-gui.desktop in ```~/.local/share/applications/```
7. Place icon in ```~/.local/share/icons/hicolor/512x512/apps/```
8. Install ```sudo apt install poppler-utils```
## Credit:
Icon created with icons from the [popos-theme](https://github.com/pop-os/icon-theme)
