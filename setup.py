# -*- coding: utf-8 -*-


"""folstamp setup module"""

from setuptools import setup

__author__ = 'Borja González Seoane'
__copyright__ = 'Copyright 2019, Borja González Seoane'
__credits__ = 'Borja González Seoane'
__license__ = 'LICENSE'
__version__ = '1.2'
__maintainer__ = 'Borja González Seoane'
__email__ = 'garaje@glezseoane.es'
__status__ = 'Development'

setup(
    name='folstamp',
    version='1.2',
    packages=['folstamp', 'folstamp.scripts'],
    entry_points={
        'console_scripts': [
            'folstamp=folstamp.__main__:main',
        ],
    },
    python_requires='>=3.6',
    install_requires=['monoshape==1.2', 'pillow==6.2.0'],
    data_files=[('util', ['util/GenericFolderIcon.png', 'util/apple.png',
                          'util/green_folder.png']),
                ('share/man/man1', ['manpages/folstamp.1']),
                ("", ["LICENSE"])],
    url='https://github.com/glezseoane/folder-stamp',
    download_url='https://github.com/glezseoane/folder-stamp/archive/v1.2.tar'
                 '.gz',
    license='LICENSE',
    author='Borja González Seoane',
    author_email='garaje@glezseoane.es',
    description='Generate custom macOS folder icons.',
    long_description='This program takes an image that has well '
                     'differentiated light and dark tones and use it to '
                     'create a custom stamped macOS folder icon.',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: MacOS',
        'Topic :: Utilities',
        'Topic :: Artistic Software',
        'Topic :: Multimedia',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Multimedia :: Graphics :: Editors',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
    ],
)
