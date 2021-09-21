import cv2
import numpy
import PIL.Image as pil_image

import data


def locate_runes(image: pil_image.Image):
    result = {}

    image_rgb = numpy.array(image.convert('RGB'))
    image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

    for rune in data.runes:
        tpl = cv2.imread(f'runes/{rune.name}.png', 0)
        w, h = tpl.shape[::-1]

        res = cv2.matchTemplate(image_gray, tpl, cv2.TM_CCOEFF_NORMED)
        loc = numpy.where(res >= 0.93)

        for pt in zip(*loc[::-1]):
            if not rune.name in result:
                result[rune.name] = []

            result[rune.name].append((pt[0], pt[1], w, h))

    return result


class RunewordMatch:

    def __init__(self, name: str, has_runes: list, missing_count: int):
        self.name = name
        self.has_runes = has_runes
        self.missing_count = missing_count

    def __repr__(self):
        return f'<RunewordMatch: {self.name}>'


# FIXME: runeword can have duplicated runes (found with "Sanctuary" (KoKoMal) might be more), code below doesn't assume it
def match_runewords(runes: dict):
    matches = []

    for word in data.runewords:
        has_runes = []
        missing_count = 0

        for name in word.runes:
            if name in runes:
                has_runes.append(name)

        missing_count = len(word.runes) - len(has_runes)

        if len(has_runes) > 0:
            matches.append(RunewordMatch(word.name, has_runes, missing_count))

    def get_missing_count(match: RunewordMatch): # TODO: maybe there is a way to move this into RunewordMatch class itself
        return match.missing_count

    matches.sort(key=get_missing_count)

    return matches
