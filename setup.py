# -*- coding: utf-8 -*-


"""folstamp setup module"""

from setuptools import setup

__author__ = 'Borja González Seoane'
__copyright__ = 'Copyright 2019, Borja González Seoane'
__credits__ = 'Borja González Seoane'
__license__ = 'LICENSE'
__version__ = '1.1'
__maintainer__ = 'Borja González Seoane'
__email__ = 'dev@glezseoane.com'
__status__ = 'Development'

setup(
    name='folstamp',
    version='1.1',
    packages=['folstamp', 'folstamp.scripts'],
    entry_points={
        'console_scripts': [
            'folstamp=folstamp.__main__:main',
        ],
    },
    python_requires='>=3.6',
    install_requires=['monoshape==1.1', 'pillow==6.1'],
    data_files=[('util', ['util/GenericFolderIcon.png', 'util/apple.png',
                          'util/green_folder.png']),
                ('share/man/man1', ['manpages/folstamp.1']),
                ("", ["LICENSE"])],
    url='https://github.com/GlezSeoane/folder-stamp',
    download_url='https://github.com/GlezSeoane/folder-stamp/archive/v1.0.1'
                 '.tar.gz',
    license='LICENSE',
    author='Borja González Seoane',
    author_email='dev@glezseoane.com',
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
