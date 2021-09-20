# from dataclasses import dataclass, field

# runes = (
#     'el', 'eld', 'tir', 'nef', 'eth', 'ith',
#     'tal', 'ral', 'ort', 'thul', 'amn', 'sol',
#     'shael', 'dol', 'hel', 'io', 'lum', 'ko',
#     'fal', 'lem', 'pul', 'um', 'mal', 'ist',
#     'gul', 'vex', 'ohm', 'lo', 'sur', 'ber',
#     'jah', 'cham', 'zod'
# )

# @dataclass
# class Rune:
#     name: str = field(req=True)
#     row: int
#     col: int


from typing import List


class Rune:
    def __init__(self, name: str, row: int, col: int):
        self.name = name
        self.row = row
        self.col = col


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
