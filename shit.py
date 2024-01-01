import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

broadcast_message = "Hello, itt az ügyfél!"
client_socket.sendto(broadcast_message.encode(), ('<broadcast>', 12345))




def send_file(conn, filename):
    with open(filename, 'rb') as file:
        data = file.read(1024)
        while data:
            conn.send(data)
            data = file.read(1024)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(1)

    print("Várakozás a kapcsolatra...")
    client_socket, client_address = server_socket.accept()
    print("Kapcsolat létrejött:", client_address)

    filename = "c:\\Users\\sibos\\Documents\\file.txt"
    send_file(client_socket, filename)

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()

client_socket.close()
