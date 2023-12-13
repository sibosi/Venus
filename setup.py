import os

repo_path = os.path.dirname(__file__)
os.chdir(repo_path)

required_directories = ['storage', 'upload']

for directory in required_directories:
    if not os.path.exists(directory):
        os.mkdir(directory)

with open('storage/log.txt', 'a') as file:
    pass

print('Setup ended.')
