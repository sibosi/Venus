import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('0.0.0.0', 12345))  # Válaszd meg egyedi portszámot
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

print("Várakozás a broadcast üzenetre...")

data, client_address = server_socket.recvfrom(1024)
print("Broadcast üzenet érkezett:", data.decode())
print("Az üzenet küldőjének címe:", client_address)





def receive_file(conn, filename):
    with open(filename, 'wb') as file:
        data = conn.recv(1024)
        while data:
            file.write(data)
            data = conn.recv(1024)

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((client_address[0], 12345))

    filename = "received_file.txt"
    receive_file(client_socket, filename)

    client_socket.close()

if __name__ == "__main__":
    main()


server_socket.close()
