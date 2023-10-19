# Inkscape Color Thief

## Overview

This Inkscape extension allows you to generate swatches
from the predominant colors within an image.
It utilizes the [color-thief-py](https://github.com/fengsp/color-thief-py)
library created by Shipeng Feng.

## Installation instructions

To install the Inkscape Color Thief extension, follow these steps:

1. Download the following files:
   - `color_colorthief.inx`
   - `color_colorthief.py`
   - `colorthief.py`

2. Place these files into your Inkscape user extension folder, which can be found at the following locations:

   - On Linux: `~/.config/inkscape/extensions`
   - On Windows: `%AppData%/inkscape/extensions`
   - On macOS: `/Users/<username>/Library/Application Support/org.inkscape.Inkscape/config/inkscape/extensions`

Pro tip: You can conveniently download the entire project as a zip file by clicking
the green `Code` button and selecting `Download ZIP`, or by visiting this link:
[Download Inkscape Color Thief](https://github.com/sherpya/inkscape-color-thief/archive/refs/heads/master.zip).

## Usage

To use this extension, follow these simple steps:

1. Open a raster image in Inkscape (prefer `Embed`, `Link` sometimes screws the original image).
2. Select the image.
3. Navigate to `Extensions` in the menu, and then choose `Color` and then `Color Thief...` from the dropdown.
4. Specify the number of colors you desire. Duplicated colors will not be added to the swatches.

## License

Copyright 2023 - Gianluigi Tiesi
This software is distributed under the terms of the BSD license.
For more details, please refer to the `LICENSE` file.
