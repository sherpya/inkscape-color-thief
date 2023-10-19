#!/usr/bin/env python3
"""
    inkscape-colorthief

    Create swatches from the color palette of an image.

    :copyright: (c) 2023 by Gianluigi Tiesi.
    :license: BSD, see LICENSE for more details.
"""
__version__ = '1.0.0'

from functools import partial
from pathlib import Path
from urllib.request import urlopen

from colorthief import ColorThief
from inkex import EffectExtension, Color, Style, Stop, LinearGradient, errormsg

XPATH_EXPR = '//svg:linearGradient[@inkscape:swatch="solid"]/svg:stop[contains(@style, "stop-color")]'


class ColorThiefExtension(EffectExtension):
    """
    Create swatches from the color palette of an image
    """

    def add_arguments(self, pars):
        pars.add_argument('--ncolors', type=int, default=16, help='Number of colors')

    def effect(self):
        svg = self.svg
        defs = svg.defs

        if len(svg.selected) != 1 or not svg.selected[0].tag.endswith('image'):
            errormsg('Select a single raster image')
            return

        image = svg.selected[0]
        xlink = image.get('xlink:href')

        # urlopen can handle data uri and file directly
        if xlink.startswith('data:') or xlink.startswith('file:'):
            opener = partial(urlopen, xlink)
        else:
            file = Path(self.options.input_file).parent / Path(xlink)
            opener = partial(file.open, 'rb')

        with opener() as f:
            color_thief = ColorThief(f)
            palette = color_thief.get_palette(color_count=self.options.ncolors)

        existing_swatches = set([Color(stop.specified_style().get('stop-color')) for stop in defs.xpath(XPATH_EXPR)])

        for index, color in enumerate(palette):
            color = Color(color)
            if color in existing_swatches:
                continue
            style = Style({'stop-color': color, 'stop-opacity': '1'})
            stop = Stop()
            stop.set('style', str(style))
            stop.set('offset', '0')
            linear_gradient = LinearGradient(stop)
            linear_gradient.set('inkscape:swatch', 'solid')
            linear_gradient.set('inkscape:label', f'swatch{index}')
            defs.append(linear_gradient)


def wait_for_debugger():
    import warnings
    warnings.filterwarnings('ignore')
    import pydevd
    import time
    while pydevd.get_global_debugger() is None or not pydevd.get_global_debugger().ready_to_run:
        time.sleep(0.3)
    breakpoint()


if __name__ == '__main__':
    # wait_for_debugger()
    ColorThiefExtension().run()
