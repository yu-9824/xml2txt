"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

# TDG

import sys
import os

from shutil import copyfile

VERSION = '0.0.1'

sys.setrecursionlimit(10 ** 9)

APP_NAME = 'xml2txt'

lib_path = os.path.join(os.environ['CONDA_PREFIX'], 'lib')
dylib_files = [os.path.join(lib_path, f) for f in os.listdir(lib_path) if '.dylib' in f]
frameworks_path = 'dist/' + APP_NAME + '.app/Contents/Frameworks'

if sys.argv[1] == 'py2app':
    from setuptools import setup

    PKG = ['pandas']

    APP = ['gui/gui.py']
    DATA_FILES = []
    OPTIONS = {
        'packages':PKG,
        'iconfile': 'gui/icon/xml2txt.icns',
        'argv_emulation': False,
        'plist': {
            'PyRuntimeLocations': [
                '@executable_path/../Frameworks/libpython3.8.dylib',
                os.path.join(lib_path, 'libpython3.8.dylib')
            ],
            'CFBundleName': APP_NAME,
            'CFBundleDisplayName': APP_NAME,
            'CFBundleGetInfoString': ".xml to .txt",
            'CFBundleIdentifier': "com.yu-9824.osx.xml2txt",
            'CFBundleVersion': VERSION,
            'CFBundleShortVersionString': VERSION,
            'NSHumanReadableCopyright': u"Copyright © 2020, yu-9824, All Rights Reserved"
        }
    }
    


    setup(
        name = 'xml2txt',
        author='yu-9824',
        version=VERSION,
        app=APP,
        data_files=DATA_FILES,
        options={'py2app': OPTIONS},
        setup_requires=['py2app'],
    )
    if len(sys.argv) >= 3 and '-A' in sys.argv:
        pass
    else:
        {copyfile(f, os.path.join(frameworks_path, os.path.basename(f))) for f in dylib_files}

