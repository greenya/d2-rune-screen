# d2-rune-screen

Diablo 2 rune helper.

## Setup

    > sudo apt-get install python3-tk
    > sudo apt-get install python3-pil.imagetk
    > pip install pillow
    > pip install pyinstaller

## Build

    > pyinstaller --onefile --windowed --clean main.py

## TODO

- [x] Main window
- [x] Paste image from clipboard, show it
    - [x] via button "Load...", allowing to browse an image
    - [x] via button "Paste"
        - [x] via CTRL+V
        - [ ] add progress or at least block ui, as pasting large image takes time and clicking Paste again breaks app
    - [ ] fix pasting image for Windows, other platforms are optional (would be nice to have)
- [x] Detect runes, locate them on image
- [ ] Show found runes in the info sidebar
- [ ] Show possible runewords
- [ ] Settings window
    - [ ] Match Ratio (%): 93 (80-98)
    - [ ] Preview Image Scale (%): 100 (25-100)
        > self.setup_preview_image(image.resize(size=(image.width//2, image.height//2)))
        > but must keep ratio and use when drawing rune locations
    - [ ] Preview Image Darken (%): 50 (0-90)
    - [ ] Font Size: 10 (8, 10, 12, 14, 16, 18)
        > root.option_add('*Font', ('', 16))
- [ ] Ability to drag image
