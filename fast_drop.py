from paths import *
import server, client
import os, json


with open('settings.json', 'r') as file:
    settings = json.load(file)


def drop_client():
    CLIENT = client.CLIENT(settings["NETWORKS"]["FAST_DROP"]["IP"],
                            settings["NETWORKS"]["FAST_DROP"]["PORT"])
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
    if drop_client() == 'go_server':
        drop_server()

main()
