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

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)
client_socket.connect(server_address)

try:
    while True:
        message = input("Enter a message to send to the server (or 'quit' to exit): ")

        if message.lower() == 'quit':
            break

        encrypted_message = caesar_cipher(message, 3)

        client_socket.send(encrypted_message.encode())

        response = client_socket.recv(1024)
        print(f"Server response: {response.decode()}")

finally:
    client_socket.close()