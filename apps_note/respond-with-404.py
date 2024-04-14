import socket


def main():
    print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    
    while True:
        conn, addr = server_socket.accept()
        recv = conn.recv(1024)
        
        print(f"got: {recv}", "\n")
        
        if (recv.decode("utf-8").split("\r\n")[0].split(" ")[1]) == "/":
            conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
        else:
            conn.send(b"HTTP/1.1 404 Not Found\r\n\r\n")
        conn.close()

        
if __name__ == "__main__":
    main()

