import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('0.0.0.0', 12345))  # Válaszd meg egyedi portszámot
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

print("Várakozás a broadcast üzenetre...")

data, client_address = server_socket.recvfrom(1024)
print("Broadcast üzenet érkezett:", data.decode())
print("Az üzenet küldőjének címe:", client_address)

