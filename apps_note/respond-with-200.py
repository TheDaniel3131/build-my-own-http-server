import socket

def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    client_socket, client_address = server_socket.accept()
    client_socket.send(b"HTTP/1.1 200 OK\r\n\r\n")
    
    
if __name__ == "__main__":
    main()