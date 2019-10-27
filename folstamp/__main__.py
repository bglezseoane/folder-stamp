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

from folstamp.scripts import gen_iconset

__author__ = 'Borja González Seoane'
__copyright__ = 'Copyright 2019, Borja González Seoane'
__credits__ = 'Borja González Seoane'
__license__ = 'LICENSE'
__version__ = '1.2'
__maintainer__ = 'Borja González Seoane'
__email__ = 'garaje@glezseoane.es'
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
    # The input path is always the first argument and it is mandatory
    mask_path = argv.pop(0)
    if not mask_path.endswith('.png'):
        raise ValueError("The mask file has to be a PNG file and has to "
                         "end with the .png extension.")
    elif not os.path.isfile(mask_path):
        raise FileNotFoundError(mask_path)

    # The output path is always the last argument and it is mandatory
    outpath = argv.pop(len(argv) - 1)
    if not outpath.endswith('.png'):
        raise ValueError("The output file has to be a PNG file and has to "
                         "end with the .png extension.")
    # elif os.path.isfile(outpath):
    #     raise FileExistsError

    # Optional black background switch
    if '-bb' in argv:
        black_background = True
        argv.remove('-bb')
    elif '--black_background' in argv:
        black_background = True
        argv.remove('--black_background')
    else:
        black_background = False

    # Optional rgb switch
    if '-rgb' in argv:
        index = argv.index('-rgb')
        red = int(argv.pop(index + 1))
        green = int(argv.pop(index + 1))
        blue = int(argv.pop(index + 1))
        argv.remove('-rgb')
    else:
        # Uses default Mojave blue to the folder stamps
        red = 90
        green = 183
        blue = 227

    # If remains some param, it should be the optional template path argument
    if len(argv) == 1:
        template_path = argv[len(argv) - 2]
        if not template_path.endswith('.png'):
            raise ValueError("The template file has to be a PNG file and has "
                             "to end with the .png extension.")
        elif not os.path.isfile(template_path):
            raise FileNotFoundError
    elif not argv:  # Uses default Mojave folder icon
        template_path = str(os.path.dirname(
            os.path.abspath(__file__)).rsplit('/', 1)[0]) \
                        + '/util/GenericFolderIcon.png'
    else:
        raise IOError("Bad command composition! Please, read the manual.")

    return mask_path, black_background, template_path, outpath, \
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
    mask_path, black_background, template_path, outpath, red, green, blue \
        = handle_arguments(sys.argv[1:])

    # Use Monoshape library to get the well format mask
    mask = extract_shape(mask_path, black_background, False,
                         True, red, green, blue)

    # Open the folder template to folstamp
    template_path = Image.open(template_path)
    template_path = template_path.convert("RGBA")

    # Stamp and save PNG
    stamped_folder = stamp(mask, template_path)
    stamped_folder.save(outpath, 'PNG')

    print(__file__)
    # Generate macOS iconset
    gen_iconset.main([outpath])

    print("[\033[92mOK\033[0m]: all generated!")


if __name__ == "__main__":
    main()
