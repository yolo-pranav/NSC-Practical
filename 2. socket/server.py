import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen(5)

while True:
    client_socket, addr = server_socket.accept()
    data = client_socket.recv(1024)
    print(f"Received: {data.decode()}")
    client_socket.send("Hello, client!".encode())
    client_socket.close()