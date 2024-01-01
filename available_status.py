import socket

class AvailabeGroup():
    def __init__(self, GROUP_CODE=8080) -> None:
        self.NEW_DEVICE_MESSAGE = '''n'''
        self.REACT_MESSAGE = '''K'''
        self.GROUP_CODE = GROUP_CODE

        self.broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # broadcast_socket.bind(('0.0.0.0', 12345))  # Válaszd meg egyedi portszámot
        self.broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        self.active = True
        self.IPGroup = []

        self.send(self.NEW_DEVICE_MESSAGE)
        while self.active:
            message, client_IP = self.listen(data_limit=10)
            if message == self.NEW_DEVICE_MESSAGE:
                self.IPGroup.append(client_IP)
                self.send(self.REACT_MESSAGE)
            

    def send(self, message : str):
        self.broadcast_socket.sendto(message.encode(), ('<broadcast>', 12345))

    def listen(self, show_message=False, data_limit=1024) -> tuple[str, str]:
        data, client_address = self.broadcast_socket.recvfrom(data_limit)
        if show_message:
            print("Broadcast üzenet érkezett:", data.decode())
            print("Az üzenet küldőjének címe:", client_address)
        return (data.decode(), client_address)

