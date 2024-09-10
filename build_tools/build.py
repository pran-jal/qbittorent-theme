import os
import subprocess

from create_resource import create_resource_file



THEME_NAME = "Night-Owl-Theme.qbtheme"
THEME_SRC_PATH = "./src"
REQUIRED_FILES = ["config.json", "stylesheet.qss"]
RESOURCE_FILE = "resource.qrc"

for file in REQUIRED_FILES:
    if not os.path.exists(f"{THEME_SRC_PATH}/{file}"):
        raise f"ERROR: Missing {file} for theme."

if not os.path.exists(f"build_tools/rcc.exe"):
    raise "ERROR: rcc.exe not found."

create_resource_file(REQUIRED_FILES, f"{THEME_SRC_PATH}/{RESOURCE_FILE}")
if not os.path.exists(f"{THEME_SRC_PATH}/{RESOURCE_FILE}"):
    raise f"ERROR: Missing {RESOURCE_FILE} for theme."

response = subprocess.run(f'build_tools/rcc.exe {THEME_SRC_PATH}/{RESOURCE_FILE} -o {THEME_NAME} -binary')
print(response)