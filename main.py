from time import sleep
import server
import threading
import json

with open('settings.json', 'r') as file:
    settings = json.load(file)

all_network = []
dict_network = {}

for network_name in settings['NETWORKS']:
    networks_settings = settings['NETWORKS'][network_name]
    if networks_settings["IP"] == None:
        if networks_settings['PUBLIC']:
            IP = server.NETWORK.local_ip
        else:
            IP = server.NETWORK.localhost
    else:
        IP = networks_settings["IP"]

    network = server.NETWORK(IP=IP, PORT=networks_settings["PORT"],
                        network_name=network_name)
    
    all_network.append(network)
    dict_network.update({network_name : network})

# 
# dict_network["SERVER1"].run()
THREAD_MAIN = threading.Thread(target=dict_network["SERVER_MAIN"].run)
THREAD_SYSTEM = threading.Thread(target=dict_network["SYSTEM"].run)

THREAD_SYSTEM.start()
THREAD_MAIN.start()


def stopable():
    while dict_network["SYSTEM"].other_info.get('run') != 'false':
        sleep(1)

    for network in all_network:
        network.shutdown_server()


STOPABLE = threading.Thread(target=stopable)
STOPABLE.start()
