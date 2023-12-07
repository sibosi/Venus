import socket
import threading

HOST = "0.0.0.0"
PORT = 8080

def handle_client(client_socket):

    data = client_socket.recv(1024)

    source_ip = client_socket.getpeername()[0]

    print(f"Received message from client ({source_ip}): {data}")
    client_socket.sendall(data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    while True:
        client_socket, client_address = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()
        server_socket.listen()
