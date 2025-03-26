import socket
import threading
import random

def game(conn):
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    num3 = random.randint(0, 10)
    conn.send(f"find sum: {num1} + {num2} + {num3} = ".encode())
    sum = num1 + num2 + num3
    print(f"sum is: {sum}")

    while True:
        user_result = int(conn.recv(1024).decode())
        if num1 + num2 + num3 == user_result:
            conn.send("congrats".encode())
            break
        else:
            conn.send("try again..".encode())
    conn.close()


def handle_client(conn, addr):
    print(f"Connection established with {addr}")
    game(conn)
    

if __name__ == "__main__":
    host = '127.0.0.1'  # Server's IP address
    port = 12346        # Server's port number

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    
    print("server is running waiting for connections")

    while True:
        conn, addr = server_socket.accept()

        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

    handle_client(conn, addr)
