import os, sys, json

required_directories = ['storage', 'upload']
packages = ["flask"]


ROOT_DIR = os.path.dirname(__file__)
PROFILE_ROOT = os.path.expanduser('~')
os.chdir(ROOT_DIR)

def setup_packages():
    # Csomagok telepítése
    # Ellenőrizzük, hogy telepítve van-e a Python.
    if not sys.version_info[:2] >= (3, 6):
        print("A Python 3.6 vagy újabb verziója szükséges.")
        sys.exit(1)

    # Telepítjük a Pip-et.
    os.system("python -m pip install --user --upgrade pip")

    # Telepítjük a szükséges csomagokat.
    for package in packages:
        os.system("python -m pip install --user {}".format(package))

def setup_dirs():
    # Mappák és fájlok létrehozása
    for directory in required_directories:
        if not os.path.exists(directory):
            os.mkdir(directory)

def setup_config():
    with open('settings.json', 'r') as file:
        full_data = json.load(file)

    # Modify the data
    path_data = {
        "ROOT" : ROOT_DIR,
        "PROFILE_ROOT" : os.path.expanduser('~'),
        "PAGE" : os.path.join(ROOT_DIR, "page"),
        "STORAGE" : os.path.join(ROOT_DIR, "storage"),
        "DROP_FROM" : os.path.join(ROOT_DIR, "fast_drop"),
        "DROP_TO" : os.path.join(PROFILE_ROOT, "drop"),
        "UPLOAD_FROM" : os.path.join(ROOT_DIR, "upload"),
        "UPLOAD_TO" : os.path.join(ROOT_DIR, "upload"),

    }
    DROP_DIR_NAME = 'drop\\'
    DROP_DIR_PATH = os.path.join(os.path.expanduser('~'), DROP_DIR_NAME)

    full_data["PATHS"] = path_data
    full_data = json.dumps(full_data, indent=4, sort_keys=True)

    # Save the modified data back to the file
    with open('settings.json', 'w') as f:
        f.write(full_data)
        # json.dump(full_data, f)



def main():
    setup_packages()
    setup_dirs()
    setup_config()
    print('Setup ended.')

if __name__ == '__main__':
    main()
