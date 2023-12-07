import socket

def send_message(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # Connect to the server
        client_socket.connect(("localhost", 8080)) # 192.168.101.

        # Send the message
        client_socket.sendall(message.encode())

        # Receive the response
        data = client_socket.recv(1024).decode()
        print(f"Received message from server: {data}")


if __name__ == "__main__":
    # Get the message from the user
    message = input("Enter the message: ")

    # Send the message to the server
    send_message(message)
