# -*- coding: utf-8 -*-


"""folstamp main

This program takes an image that has well differentiated light and dark
tones and use it to create a custom stamped macOS folder icon.

This is the main Python file.
"""

import os
import sys
from copy import deepcopy
from typing import Tuple, List

from PIL import Image
from monoshape.__main__ import extract_shape

__author__ = 'Borja González Seoane'
__copyright__ = 'Copyright 2019, Borja González Seoane'
__credits__ = 'Borja González Seoane'
__license__ = 'LICENSE'
__version__ = '0.1dev0'
__maintainer__ = 'Borja González Seoane'
__email__ = 'dev@glezseoane.com'
__status__ = 'Development'


# =============================================
# =               Order handling              =
# =============================================
# noinspection PyShadowingNames
def handle_arguments(argv: List) -> Tuple:
    """Handles the arguments.

    Handles the arguments when the program is run and exports it into a
    enumeration of it.

    :param argv: Vector with the ordered input arguments
    :type argv: List
    :return: Interpreted argument vector
    :rtype: Tuple
    """
    # Assert composition integrity
    if len(argv) < 3 or len(argv) > 8:
        raise IOError("Bad command composition! Please, read the manual.")

    # The input path is always the first argument
    mask_path = argv[1]
    if not mask_path.endswith('.png'):
        raise ValueError("The mask file has to be a PNG file and has to "
                         "end with the .png extension.")
    elif not os.path.isfile(mask_path):
        raise FileNotFoundError

    # The template path is always the second last argument
    template_path = argv[len(argv) - 2]
    if not template_path.endswith('.png'):
        raise ValueError("The template file has to be a PNG file and has to "
                         "end with the .png extension.")
    elif not os.path.isfile(template_path):
        raise FileNotFoundError

    # The output path is always the last argument
    outpath = argv[len(argv) - 1]
    if not outpath.endswith('.png'):
        raise ValueError("The output file has to be a PNG file and has to "
                         "end with the .png extension.")
    # elif os.path.isfile(outpath):
    #     raise FileExistsError

    black_background = '-bb' in argv or '--black_background' in argv

    if '-rgb' in argv:
        rgb_shape = True
        index = argv.index('-rgb')
        red = int(argv[index + 1])
        green = int(argv[index + 2])
        blue = int(argv[index + 3])
    else:
        rgb_shape = False
        # Uses default Mojave blue to the folder stamps
        red = 82
        green = 145
        blue = 189

    return mask_path, black_background, template_path, outpath, rgb_shape, \
        red, green, blue


# =============================================
# =                  Process                  =
# =============================================
def stamp(mask: 'Image.Image', background_folder: 'Image.Image') \
        -> 'Image.Image':
    """Stamps a mask on a background folder template

    :param mask: Mask to folstamp
    :type mask: 'Image.Image'
    :param background_folder: Background folder template
    :type background_folder: 'Image.Image'
    :return: Stamped folder image
    :rtype: 'Image.Image'
    """
    mask = deepcopy(mask)
    mask = mask.resize((500, 500))

    stamped_folder = deepcopy(background_folder)
    stamped_folder = stamped_folder.resize((1024, 1024))
    stamped_folder.paste(mask, (262, 300), mask)
    return stamped_folder


# =============================================
# =                    MAIN                   =
# =============================================
def main():
    mask_path, black_background, template_path, outpath, rgb_shape, red, \
        green, blue = handle_arguments(sys.argv)

    mask = extract_shape(mask_path, black_background, False,
                         rgb_shape, red, green, blue)

    # Open the folder template to folstamp
    template_path = Image.open(template_path)
    template_path = template_path.convert("RGBA")

    stamped_folder = stamp(mask, template_path)
    stamped_folder.save(outpath, 'PNG')


if __name__ == "__main__":
    main()
