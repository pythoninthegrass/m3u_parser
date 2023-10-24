#!/usr/bin/env python3

import PyInstaller.__main__
from pathlib import Path

here = Path(__file__).parent.absolute()
path_to_main = str(here / "main.py")


def install():
    PyInstaller.__main__.run([
        path_to_main,
        '--name=m3u-parsr',
        '--onefile',
        '--nowindow',
        '--add-data=README.md:.',
        '--workpath=/tmp',
    ])
