# Original by Fabulously Optimized
# Edited for my use case

import json
import toml
from pathlib import Path

version = input("Input version you'd like to update: ")

# so this one get the path of main menu credit config and the modpack folder
version_path = Path.home() / f"Desktop/FEV/versions/{version}"
title_screen_path = version_path / "configureddefaults/config/isxander-main-menu-credits.json"

# this one load toml file
with open(f'{version_path}/pack.toml', 'r') as f:
    packtoml = toml.load(f)

# these guys is a function for loading json file and writing them
def load_json(path: Path) -> dict:
    with open(path, "r") as f:
        return json.load(f)

def save_file(path: Path, obj) -> None:
    with open(path, "w") as f:
        json.dump(obj, f, separators=(",", ":"))

# this load the json and toml
title_screen_obj = load_json(title_screen_path)
existing_version = title_screen_obj["main_menu"]["bottom_left"][0]
curfabrver = packtoml['versions']['fabric']
curmdpkver = packtoml['version']

# this guy ask for the new version
print(f"Current fabric version: {curfabrver}")
fabricver = input("Enter latest fabric version: ")
print(f"Current modpack version: {curmdpkver}")
modpackver = input("Enter new modpack version: ")

# it write it on the clipboard (idk what's it's called but it's not in the file yet)
packtoml['versions']['fabric'] = f'{fabricver}'
packtoml['version'] = f'{modpackver}'

# this is for main menu credit
print(f"Current version: {existing_version}")
new_version = input("Enter new version: Fuzzy's Enhanced Vanilla ")

# these write them into the files
title_screen_obj["main_menu"]["bottom_left"][0] = f"Fuzzy's Enhanced Vanilla {new_version}"
save_file(title_screen_path, title_screen_obj)

with open(f'{version_path}/pack.toml', 'w') as f:
    toml.dump(packtoml, f)

# this is for the check
newmdpkver = title_screen_obj["main_menu"]["bottom_left"][0]
with open('pack.toml', 'r') as f:
    packtoml = toml.load(f)

print("----- Update check -----")
print(packtoml['versions']['fabric'])
print(packtoml['version'])
print(newmdpkver)