from datetime import datetime
print(f'{datetime.now()} | Venus update started')


import os
import subprocess


repo_path = os.path.dirname(__file__)
os.chdir(repo_path)
subprocess.run(['git', 'pull'])


print(f'{datetime.now()} | Venus update ended\n')

#subprocess.run(['python', 'check-in.py', '>>',  '~/log.txt',  '&'])
