import os
import subprocess


THEME_NAME = "Night-Owl-Theme.qbtheme"


cmd = ['rcc.exe', 'resource.qrc', '-o', THEME_NAME,  '-binary']
response = subprocess.call(cmd)