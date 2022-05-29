"""
Author: cxy
Date: 2022/01/28
"""
import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os", "datetime", "redis"], "includes": ["tkinter"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="高光谱数据接收软件",
    version="1.0",
    description="接收数据",
    options={"build_exe": build_exe_options},
    executables=[Executable("recDataGUI.py", base=base)]
)
