""" SETUP.py (cx_Freeze) """

import sys
import os
from cx_Freeze import setup, Executable

includefiles = ["images", "scripts", "config"]

packages = ["os", "pygame", "sys"]

options = {
            "include_files": includefiles,
            "packages": packages,
          }

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "MacGyver",
        version = "1.0",
        description = "MacGyver Game!",
        options = {"build_exe": options},
        executables = [Executable("game.py", base=base)])
