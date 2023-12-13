import subprocess
import time
import json


with open('settings.json', 'r') as file:
    settings = json.load(file)

for i in range(10, 0, -1):
    print(f'Biztosan törölni szeretnéd az egész programot? [{i}]', end='\r')
    time.sleep(1)

valasz = None
while valasz not in settings["ANSWERS"]["yes"] and \
        valasz not in settings["ANSWERS"]["no"]:
    valasz = input('Biztosan törölni szeretnéd az egész programot? [y / n] ')

if valasz in settings["ANSWEARS"]["yes"]:
    subprocess.run('git rm -r --cached .'.split(' '))
    subprocess.run('rm -rf .git'.split(' '))
    print('The repository has been deleted.')
else:
    print('The repository is still alive.')
