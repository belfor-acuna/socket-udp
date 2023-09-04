import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
server_host = "127.0.0.1";
server_port = 10500;

while True:
    message = input("Mensaje: ");
    client_socket.sendto(message.encode('utf-8'), (server_host, server_port));
    response, server_address = client_socket.recvfrom(1024);
    print(f"Respuesta del servidor: {response.decode('utf-8')}");
