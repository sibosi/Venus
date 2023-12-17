import os
import sys

required_directories = ['storage', 'upload']
packages = ["bottle", "flask"]


repo_path = os.path.dirname(__file__)
os.chdir(repo_path)

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


# Mappák és fájlok létrehozása
for directory in required_directories:
    if not os.path.exists(directory):
        os.mkdir(directory)

with open('storage/log.txt', 'a') as file:
    pass

print('Setup ended.')
