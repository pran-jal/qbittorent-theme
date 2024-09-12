import os
import subprocess

from create_resource import create_resource_file



THEME_NAME = "Night-Owl-Theme.qbtheme"
THEME_SRC_PATH = "./src"
REQUIRED_FILES = [{"name":"config.json"}, {"alias": "stylesheet.qss", "name": "stylesheet.qss"}]
RESOURCE_FILE = "resource.qrc"

for file in REQUIRED_FILES:
    if not os.path.exists(f"{THEME_SRC_PATH}/{file['name']}"):
        raise Exception(f"ERROR: Missing {file['name']} for theme.")
        exit()

if not os.path.exists(f"build_tools/rcc.exe"):
    raise Exception("ERROR: rcc.exe not found.")
    exit()

create_resource_file(REQUIRED_FILES, f"{THEME_SRC_PATH}/{RESOURCE_FILE}")
if not os.path.exists(f"{THEME_SRC_PATH}/{RESOURCE_FILE}"):
    raise Exception(f"ERROR: Missing {RESOURCE_FILE} for theme.")
    exit()

response = subprocess.run(f'build_tools/rcc.exe {THEME_SRC_PATH}/{RESOURCE_FILE} -o {THEME_NAME} -binary')
print(response)