import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
server_host = "127.0.0.1"; 
server_port = 10500;  

server_socket.bind((server_host, server_port));

print(f"Servidor escuchando en {server_host}:{server_port}");

while True:
    data, client_address = server_socket.recvfrom(1024);
    print(f"Recibido desde {client_address}: {data.decode('utf-8')}");
    response = "Recibido desde el servidor";
    server_socket.sendto(response.encode('utf-8'), client_address);
