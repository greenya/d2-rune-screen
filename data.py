from typing import List


# TODO: add "recipe"
class Rune:

    def __init__(self, name: str, row: int, col: int):
        self.name = name
        self.row = row
        self.col = col

    def __repr__(self):
        return f'<Rune: {self.name}>'


runes: List[Rune] = [
    Rune(name='el', row=0, col=0),
    Rune(name='eld', row=0, col=1),
    Rune(name='tir', row=0, col=2),
    Rune(name='nef', row=0, col=3),
    Rune(name='eth', row=0, col=4),
    Rune(name='ith', row=1, col=0),
    Rune(name='tal', row=1, col=1),
    Rune(name='ral', row=1, col=2),
    Rune(name='ort', row=1, col=3),
    Rune(name='thul', row=1, col=4),
    Rune(name='amn', row=2, col=0),
    Rune(name='sol', row=2, col=1),
    Rune(name='shael', row=2, col=2),
    Rune(name='dol', row=2, col=3),
    Rune(name='hel', row=2, col=4),
    Rune(name='io', row=3, col=0),
    Rune(name='lum', row=3, col=1),
    Rune(name='ko', row=3, col=2),
    Rune(name='fal', row=3, col=3),
    Rune(name='lem', row=3, col=4),
    Rune(name='pul', row=4, col=0),
    Rune(name='um', row=4, col=1),
    Rune(name='mal', row=4, col=2),
    Rune(name='ist', row=4, col=3),
    Rune(name='gul', row=4, col=4),
    Rune(name='vex', row=5, col=0),
    Rune(name='ohm', row=5, col=1),
    Rune(name='lo', row=5, col=2),
    Rune(name='sur', row=5, col=3),
    Rune(name='ber', row=5, col=4),
    Rune(name='jah', row=6, col=0),
    Rune(name='cham', row=6, col=1),
    Rune(name='zod', row=6, col=2)
]


# TODO: add "gear" and "stats"
class Runeword:

    def __init__(self, name: str, runes: List[str], level: int):
        self.name = name
        self.runes = runes
        self.level = level
        self.word = ''.join(x.title() for x in self.runes)

    def __repr__(self):
        return f'<Runeword: {self.name}>'


# TODO: add all runes
runewords: List[Runeword] = [
    Runeword(name='Ancient\'s Pledge', runes=[ 'ral', 'ort', 'tal' ], level=21),
    Runeword(name='Edge', runes=[ 'tir', 'tal', 'amn' ], level=25),
    Runeword(name='Gloom', runes=[ 'fal', 'um', 'pul' ], level=47),
    Runeword(name='Holy Thunder', runes=[ 'eth', 'ral', 'ort', 'tal' ], level=23),
    Runeword(name='Insight', runes=[ 'ral', 'tir', 'tal', 'sol' ], level=27),
    Runeword(name='King\'s Grace', runes=[ 'amn', 'ral', 'thul' ], level=25),
    Runeword(name='Lore', runes=[ 'ort', 'sol' ], level=27),
    Runeword(name='Leaf', runes=[ 'tir', 'ral' ], level=19),
    Runeword(name='Malice', runes=[ 'ith', 'el', 'eth' ], level=15),
    Runeword(name='Nadir', runes=[ 'nef', 'tir' ], level=13),
    Runeword(name='Radiance', runes=[ 'nef', 'sol', 'ith' ], level=27),
    Runeword(name='Spirit', runes=[ 'tal', 'thul', 'ort', 'amn' ], level=25),
    Runeword(name='Stealth', runes=[ 'tal', 'eth' ], level=17),
    Runeword(name='Steel', runes=[ 'tir', 'el' ], level=13),
    Runeword(name='Strength', runes=[ 'amn', 'tir' ], level=25),
    Runeword(name='Zephyr', runes=[ 'ort', 'eth' ], level=21)
]
