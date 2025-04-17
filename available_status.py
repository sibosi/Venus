import socket
from time import sleep

class AvailabeGroup():
    def __init__(self, GROUP_CODE=12345) -> None:
        self.NEW_DEVICE_MESSAGE = '''n'''
        self.REACT_MESSAGE = '''K'''
        self.GROUP_CODE = GROUP_CODE

        self.hostname = socket.gethostname()
        self.IPAdress = socket.gethostbyname_ex(self.hostname)[-1][-1]

        self.broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.broadcast_socket.bind(('0.0.0.0', self.GROUP_CODE))  # Válaszd meg egyedi portszámot
        self.broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # self.broadcast_socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.active = True
        self.IPGroup = []


    def send(self, message : str):
        self.broadcast_socket.sendto(message.encode(), ('<broadcast>', self.GROUP_CODE))
        print('Sended', message.encode(), self.GROUP_CODE)

    def listen(self, show_message=False, data_limit=1024) -> tuple[str, str]:
        # self.broadcast_socket.bind(('0.0.0.0', 54321))  # Válaszd meg egyedi portszámot
        # self.broadcast_socket.settimeout(5)
        # while self.active:
        # try:
        # print('Ready to listen')
        # self.send('Hi e')
        data, client_address = self.broadcast_socket.recvfrom(data_limit)
        # print('SIker: ', data.decode(), client_address)
        # except socket.timeout:
        #    pass

        if show_message:
            # print("Broadcast üzenet érkezett:", data.decode())
            # print("Az üzenet küldőjének címe:", client_address)
            if client_address[0] != self.IPAdress:
                print(str(client_address) + ': ' + data.decode())
                print(self.IPGroup)
                print('')
        
        if not self.active:
            return (None, None)
        
        return (data.decode(), client_address)
    
    def join(self):
        self.send(self.NEW_DEVICE_MESSAGE)

    def joinLiveGroup(self, data_limit=10, show_message=False):
        import threading
        print(str(self.broadcast_socket))

        def liveGroup():
            self.join()
            while self.active:
                message, client_IP = self.listen(data_limit=data_limit, show_message=show_message)
                if message == self.NEW_DEVICE_MESSAGE:
                    self.IPGroup.append(client_IP)
                    self.send(self.REACT_MESSAGE)
        
        liveThread = threading.Thread(target=liveGroup)
        liveThread.start()

if __name__ == '__main__':
    AG = AvailabeGroup()
    AG.joinLiveGroup(1024, show_message=True)
