import json

with open('settings.json', 'r') as file:
    settings = json.load(file)


all_path = settings["PATHS"]

ROOT_DIR = all_path["ROOT"]
PROFILE_ROOT_DIR = all_path["PROFILE_ROOT"]
STORAGE_DIR = all_path["STORAGE"]
PAGE_DIR = all_path["PAGE"]
DROP_FROM_DIR = all_path["DROP_FROM"]
DROP_TO_DIR = all_path["DROP_TO"]
UPLOAD_FROM_DIR = all_path["UPLOAD_FROM"]
UPLOAD_TO_DIR = all_path["UPLOAD_TO"]
