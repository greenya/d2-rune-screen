# d2-rune-screen

Diablo 2 rune helper.

## Setup

```sh
# Linux
sudo apt-get install python3-tk python3-venv
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt

# Windows
winget install --exact --id Python.Python.3.14 --source winget
# Reopen terminal in the project directory after installing Python
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Run

```sh
# Linux
.venv/bin/python src/main.py

# Windows
.venv\Scripts\python.exe src\main.py
```

## Build

```sh
pyinstaller --onefile --windowed --clean --add-data "runes:runes" --add-data "examples:examples" src/main.py
```

## TODO

- [x] Main window
- [x] Paste image from clipboard, show it
    - [x] via button "Load...", allowing to browse an image
    - [x] via button "Paste"
        - [x] via CTRL+V
        - [ ] add progress or at least block ui, as pasting large image takes time and clicking Paste again breaks app
    - [ ] fix pasting image for Windows, other platforms are optional (would be nice to have)
- [x] Detect runes, locate them on image
- [x] Show found runes in the info sidebar
- [x] Show possible runewords
- [ ] Settings window
    - [ ] Match Ratio (%): 93 (80-98)
    - [ ] Preview Image Scale (%): 100 (25-100)
        > self.setup_preview_image(image.resize(size=(image.width//2, image.height//2)))
        > but must keep ratio and use when drawing rune locations
    - [ ] Preview Image Darken (%): 50 (0-90)
    - [ ] Font Size: 10 (8, 10, 12, 14, 16, 18)
        > root.option_add('*Font', ('', 16))
- [ ] Ability to drag image
