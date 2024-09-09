import os
import subprocess



THEME_NAME = "Night-Owl-Theme.qbtheme"
THEME_SRC_PATH = "./src"
REQUIRED_FILES = ["resource.qrc", "config.json", "stylesheet.qss"]

for file in REQUIRED_FILES:
    if not os.path.exists(f"{THEME_SRC_PATH}/{file}"):
        raise f"ERROR: Missing {file} for theme."

if not os.path.exists(f"build_tools/rcc.exe"):
    raise "ERROR: rcc.exe not found."

response = subprocess.run(f'build_tools/rcc.exe ./src/resource.qrc -o {THEME_NAME} -binary')