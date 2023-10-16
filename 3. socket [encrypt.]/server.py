import socket

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            result += chr(((ord(char) - offset + shift) % 26) + offset)
        else:
            result += char
    return result

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)
server_socket.bind(server_address)

server_socket.listen(5)
print("Server is listening for incoming connections...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    try:
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break

            decrypted_data = caesar_cipher(data, -3)

            print(f"Received message from client: {decrypted_data}")

            response = f"Server received and decrypted: {decrypted_data}"
            client_socket.send(response.encode())

    finally:
        print(f"Closing connection from {client_address}")
        client_socket.close()