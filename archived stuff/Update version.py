# Original by Fabulously Optimized
# Edited for my use case

import json
import toml
from pathlib import Path

version = input("Input version you'd like to update > ")

version_path = Path.home() / f"Desktop/Modpack/FEV/versions/{version}"
title_screen_path = version_path / "config/isxander-main-menu-credits.json"
packtoml_path = version_path / "pack.toml"

def load_toml(path: Path) -> dict:
    with open(path, "r") as f:
        return toml.load(f)
    
def load_json(path: Path) -> dict:
    with open(path, "r") as f:
        return json.load(f)f
    
def save_toml(path: Path, obj) -> None:
    with open(path, "w") as f:
        toml.dump(obj, f)

def save_json(path: Path, obj) -> None:
    with open(path, "w") as f:
        json.dump(obj, f, separators=(",", ":"))

title_screen_obj = load_json(title_screen_path)
packtoml = load_toml(packtoml_path)
existing_version = title_screen_obj["main_menu"]["bottom_left"][0]
current_fabric_version = packtoml["versions"]["fabric"]
current_modpack_version = packtoml["version"]

print(f"Current fabric version: {current_fabric_version}")
new_fabric_version = input("Enter latest fabric version (leave blank for current version) > ") or current_fabric_version
print(f"Current modpack version: {current_modpack_version}")
new_modpack_version = input("Enter new modpack version > ")
print(f"Current version: {existing_version}")
new_version = input("Enter new version > Fuzzy's Enhanced Vanilla ")

packtoml["versions"]["fabric"] = f"{new_fabric_version}"
packtoml["version"] = f"{new_modpack_version}"
title_screen_obj["main_menu"]["bottom_left"][0] = f"Fuzzy's Enhanced Vanilla {new_version}"

save_toml(packtoml_path, packtoml)
save_json(title_screen_path, title_screen_obj)