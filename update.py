from datetime import datetime
import os, json, subprocess
from paths import *

def main():

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

    os.chdir(ROOT_DIR)
    subprocess_update(['git', 'pull'])

    print_update(f'{datetime.now()} | Venus update ended\n')

    if settings["check-in after update"]:
        import client
        CLIENT_UPDATE = client.NETWORK(IP=settings["NETWORKS"]["SERVER_UPDATE"]["IP"],
                       PORT=settings["NETWORKS"]["SERVER_UPDATE"]["PORT"])
        try:
            CLIENT_UPDATE.chat(message= 'Venus updated - restart the server')
            CLIENT_UPDATE.chat(message= 'check-out')
        except:
            pass
        subprocess.run(['python', 'check-in.py', '>>',  'storage/log.txt',  '&'])

if __name__ == '__main__':
    main()
