from email import message
import requests
import os

root_dir = os.path.dirname(__file__)


class CLIENT():
    def __init__(self, IP=None, PORT=None) -> None:
        if IP == None:
            IP = input('Enter the IP: ')
        if PORT == None:
            IP = input('Enter the PORT: ')
        
        self.IP = IP
        self.PORT = PORT
    
    def upload_file(self, file_name=None):
        # Készítsen HTTP POST kérést a szerverhez
        if file_name == None:
            file_name = input('Enter the path of the file to upload: ')
        file_path=os.path.join(root_dir, file_name)


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
    
    def chat(self, message=None):
        import socket

        if message == None:
            message = input('Send a message: ')

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.IP, self.PORT))

        # A kérés felépítése HTTP POST kérés formájában
        request = f'POST /chat HTTP/1.1\r\nContent-Type: text/plain\r\nContent-Length: {len(message)}\r\n\r\n{message}'
        client_socket.sendall(request.encode())

        # A válasz beolvasása
        response = client_socket.recv(1024)

        # A válasz kiírása
        print(response.decode())

        # A kapcsolat lezárása
        client_socket.close()
    
    def run(self):
        valasz = input('Chat or file sending (c or f): ')
        while valasz == 'c' or valasz == 'f':
            if valasz == 'f':
                self.upload_file()
            else:
                self.chat()
            valasz = input('Chat or file sending (c or s)')
            


if __name__ == '__main__':
    client1 = CLIENT()
    client1.run()
