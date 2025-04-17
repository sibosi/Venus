from time import sleep
from paths import *
import available_status
import server, client
import os, json


with open('settings.json', 'r') as file:
    settings = json.load(file)


def drop_client(IP : str):
    CLIENT = client.CLIENT(IP, settings["NETWORKS"]["FAST_DROP"]["PORT"])
    try:
        CLIENT.chat('Client avaiable')
    except:
        return 'go_server'
    CLIENT.upload_directory(DROP_FROM_DIR)
    print(f'Directory {DROP_FROM_DIR} dropped!')

def drop_server():
    if not os.path.exists(DROP_TO_DIR):
        os.mkdir(DROP_TO_DIR)
    
    SERVER = server.NETWORK(settings["NETWORKS"]["FAST_DROP"]["IP"],
                            settings["NETWORKS"]["FAST_DROP"]["PORT"],
                            network_name='drop_server',
                            upload_directory_path=DROP_TO_DIR)
    SERVER.run()

def main():
    available = available_status.AvailabeGroup()
    available.joinLiveGroup(data_limit=1024, show_message=True)
    for _ in range(10):
        if len(available.IPGroup) > 0:
            drop_client(available.IPGroup[0])
        sleep(0.5)
    drop_server()
    available.active = False

main()
