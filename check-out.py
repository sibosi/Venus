# It can chenck out only from the main.py
import client
import json

def main():
    with open('settings.json', 'r') as file:
        settings = json.load(file)
    
    CLIENT = client.CLIENT(settings["NETWORKS"]["SYSTEM"]["IP"],
                           settings["NETWORKS"]["SYSTEM"]["PORT"])
    CLIENT.chat('SYSTEM-SET run false')
    # Üzenet a szervernek --> leállítás

if __name__ == '__main__':
    main()
