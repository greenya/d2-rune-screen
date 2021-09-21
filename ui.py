from textwrap import fill
from typing import List
import io
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import PIL.Image as pil_image
import PIL.ImageTk as pil_image_tk

import data
import util


def open(title: str, geometry: str):
    root = tk.Tk()
    root.title(title)
    root.geometry(geometry)

    MainWindow(root)
    root.mainloop()


class MainWindow:

    def __init__(self, parent: tk.Frame):
        self.root = tk.Frame(parent)
        self.root.pack(fill='both', expand=True)

        self.root.bind_all('<<Paste>>', lambda _: self.paste_click())

        ## header

        self.header = tk.Frame(self.root)
        self.header.pack(side='top', fill='x')

        button_paste = tk.Button(self.header, command=self.paste_click, text='Paste from Clipboard')
        button_paste.pack(side='left')

        button_load = tk.Button(self.header, command=self.load_click, text='Load from file...')
        button_load.pack(side='left')

        button_settings = tk.Button(self.header, command=self.settings_click, text='Settings...')
        button_settings.pack(side='right')

        ## middle

        self.middle = tk.Frame(self.root, bd=2)
        self.middle.pack(side='top', fill='both', expand=True)

        # middle > sidebar

        # TODO: make sidebar vertically scrollable
        self.sidebar = tk.Frame(self.middle)

        self.runes_bar = tk.Frame(self.sidebar)
        self.runes_bar.pack(side='top', fill='x')

        for rune in data.runes:
            label = tk.Label(self.runes_bar, name=rune.name, relief=tk.RAISED, width=6)
            label.grid(row=rune.row, column=rune.col)
            self.setup_rune_count(rune.name, 0)

        self.runewords_bar = tk.Frame(self.sidebar)
        self.runewords_bar.pack(side='top', fill='x')

        self.sidebar.pack(side='left', fill='y')

        # middle > canvas

        self.canvas = tk.Canvas(self.middle)

        hbar = tk.Scrollbar(self.middle, orient='horizontal', command=self.canvas.xview)
        hbar.pack(side='bottom', fill='x')

        vbar = tk.Scrollbar(self.middle, orient='vertical', command=self.canvas.yview)
        vbar.pack(side='right', fill='y')

        self.canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.canvas.pack(expand=True)

        self.setup_new_image(pil_image.open('/home/lexx/Projects/d2-rune-screen/examples/6.jpg')) # ! DEBUG

    def load_click(self):
        filename = tkinter.filedialog.askopenfilename(
            title='Open an image',
            filetypes=(
                ('Images', '*.png *.jpg *.jpe *.jpeg *.bmp'),
                ('All files', '*.*')
            )
        )

        if filename:
            image = pil_image.open(filename)
            self.setup_new_image(image)

    def paste_click(self):
        try:
            bytes = bytearray()
            byte = ''

            for c in self.root.selection_get(selection='CLIPBOARD', type='image/png'):
                if c == ' ':
                    bytes.append(int(byte, 0))
                    byte = ''
                else:
                    byte += c

            with pil_image.open(io.BytesIO(bytes)) as image:
                self.setup_new_image(image)

        except tk.TclError as e:
            print(f'TclError: {e}')
            tkinter.messagebox.showerror(message='Failed to interpret Clipboard content as an image.')

    def setup_new_image(self, image: pil_image.Image):
        self.setup_preview_image(image)
        self.setup_sidebar(image)

    def setup_preview_image(self, image: pil_image.Image):
        self.preview_image = pil_image_tk.PhotoImage(image)
        width = self.preview_image.width()
        height = self.preview_image.height()
        self.canvas.configure(width=width, height=height, scrollregion=(0, 0, width, height))
        self.canvas.create_image(0, 0, image=self.preview_image, anchor='nw')
        self.shade_canvas()

    def shade_canvas(self):
        width, height = self.preview_image.width(), self.preview_image.height()
        image = pil_image.new('RGBA', (width, height), (0, 0, 0, 0xbb))
        self.shade_image = pil_image_tk.PhotoImage(image)
        self.canvas.create_image(0, 0, image=self.shade_image, anchor='nw')

    def setup_sidebar(self, image: pil_image.Image):
        found_runes = util.locate_runes(image)
        self.mark_runes_canvas(found_runes)
        self.setup_runes_sidebar(found_runes)
        found_words = util.match_runewords(found_runes)
        self.setup_runewords_sidebar(found_words)

    def mark_runes_canvas(self, found_runes: dict):
        for name in found_runes:
            for (x, y, w, h) in found_runes[name]:
                self.canvas.create_rectangle(x, y, x+w, y+h, outline='red')

    def setup_runes_sidebar(self, found_runes: dict):
        for rune in data.runes:
            count = 0
            if rune.name in found_runes:
                count = len(found_runes[rune.name])

            self.setup_rune_count(rune.name, count)

    def setup_runewords_sidebar(self, matches: List[util.RunewordMatch]):
        for widget in self.runewords_bar.winfo_children():
            widget.destroy()

        for match in matches:
            print(match, match.missing_count, match.has_runes)

            # TODO: make list of runes, show what is missing with dimmed color
            label = tk.Label(self.runewords_bar, text=f'{match.name}\n{match.has_runes} -- missing: {match.missing_count}', relief=tk.RAISED)
            label.pack(side='top', fill='x')

    def setup_rune_count(self, rune_name, rune_count):
        widget = self.runes_bar.children[rune_name]
        widget['text'] = f'{rune_name.capitalize()}\nx{rune_count}'
        if rune_count > 0:
            widget['state'] = tk.NORMAL
        else:
            widget['state'] = tk.DISABLED

    def settings_click(self):
        tkinter.messagebox.showinfo(message='Settings window not implemented yet.')


# class SettingsWindow:
#     pass
