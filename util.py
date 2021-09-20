import cv2
import numpy
import PIL.Image as pil_image

import data


def locate_runes_in_image(image: pil_image.Image):
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
