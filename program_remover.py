import os
import shutil
import stat
import time
import json

with open('settings.json', 'r') as file:
    settings = json.load(file)

repo_path = os.path.dirname(__file__)
os.chdir(repo_path)

for i in range(10, 0, -1):
    print(f'Biztosan törölni szeretnéd az egész programot? [{i}]', end='\r')
    time.sleep(1)

valasz = None
while valasz not in settings["ANSWERS"]["yes"] and \
        valasz not in settings["ANSWERS"]["no"]:
    valasz = input('Biztosan törölni szeretnéd az egész programot? [y / n] ')

if valasz in settings["ANSWERS"]["yes"]:
    for root, dirs, files in os.walk(repo_path):  
        for dir in dirs:
            os.chmod(os.path.join(root, dir), stat.S_IRWXU)
        for file in files:
            os.chmod(os.path.join(root, file), stat.S_IRWXU)
    shutil.rmtree(repo_path)

    print('The repository has been deleted.')
else:
    print('The repository is still alive.')
