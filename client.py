import socket
import requests
import os
from paths import *


class CLIENT():
    def __init__(self, IP='localhost', PORT=None) -> None:
        if IP == None:
            IP = input('Enter the IP: ')
        if PORT == None:
            PORT = int(input('Enter the PORT: '))
        
        if IP == '0.0.0.0':
            IP = socket.gethostbyname_ex(socket.gethostname())[-1][-1]

        self.IP = IP
        self.PORT = PORT
    
    def upload_file(self, file_name=None):
        # Készítsen HTTP POST kérést a szerverhez
        if file_name == None:
            print(f'Upload the file from here: {ROOT_DIR}')
            print("""Enter a "*" to upload from your profile's rootdir!""")
            file_name = input('Enter the name of the file to upload: ')
            if file_name == "*":
                print(f'Upload the file from here: {PROFILE_ROOT_DIR}')
                file_name = input('Enter the name of the file to upload: ')
                file_path=os.path.join(PROFILE_ROOT_DIR, file_name)
            else:
                file_path=os.path.join(ROOT_DIR, file_name)

        else:
            file_path=os.path.join(ROOT_DIR, file_name)


        request = requests.post(f'http://{self.IP}:{self.PORT}/upload', files={'file': open(file_path, 'rb')})

        # Ellenőrizze a válasz kódját
        if request.status_code == 200:
            # A fájl sikeresen feltöltésre került
            print('A fájl sikeresen feltöltésre került.')
            return True
        else:
            # A fájl feltöltése sikertelen
            print('A fájl feltöltése sikertelen.')
            return False
    
    def upload_directory(self, directory_path=None):
        if directory_path == None:
            directory_path = input('Enter the path of the dir to upload: ')
        for file in os.listdir(directory_path):
            try:
                self.upload_file(file)
            except:
                self.chat(f'The file {file} not able to upload.')


    def chat(self, message=None):
        import socket

        if message == None:
            message = input('Send a message: ')

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            client_socket.connect((self.IP, self.PORT))
        except ConnectionRefusedError:
            print('ConnectionRefusedError: Nem hozható létre kapcsolat, mert a célszámítógép már visszautasította a kapcsolatot.')
            exit()

        # A kérés felépítése HTTP POST kérés formájában
        request = f'POST /chat HTTP/1.1\r\nContent-Type: text/plain\r\nContent-Length: {len(message)}\r\n\r\n{message}'
        client_socket.sendall(request.encode())

        # A válasz beolvasása
        response = client_socket.recv(1024)

        # A válasz kiírása
        print(response.decode().split('\n')[0])

        # A kapcsolat lezárása
        client_socket.close()
    
    def run(self):
        valasz = input('Chat or file sending (c or f): ')
        while valasz == 'c' or valasz == 'f':
            if valasz == 'f':
                self.upload_file()
            else:
                self.chat()
            valasz = input('Chat or file sending (c or f)')
            


if __name__ == '__main__':
    client1 = CLIENT(PORT=8080)
    client1.run()
