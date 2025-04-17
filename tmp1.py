import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

broadcast_message = "Hello, itt az ügyfél!"
client_socket.sendto(broadcast_message.encode(), ('<broadcast>', 12345))
