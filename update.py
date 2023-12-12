from datetime import datetime
import json
import os
import subprocess
import sys


with open('settings.json', 'r') as file:
    settings = json.load(file)

def print_update(*a):
    if settings["update printing"]:
        print(*a)
    if settings["update logging"]:
        with open('storage/log.txt', 'a') as file:
            file.write(*a)
            file.write('\n')

def subprocess_update(command):
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        output, err = process.communicate()

        print_update(str(output))    


print_update(f'{datetime.now()} | Venus update started')

repo_path = os.path.dirname(__file__)
os.chdir(repo_path)
subprocess_update(['git', 'pull'])

print_update(f'{datetime.now()} | Venus update ended\n')

if settings["check-in after update"]:
    subprocess.run(['python', 'check-in.py', '>>',  'storage/log.txt',  '&'])
