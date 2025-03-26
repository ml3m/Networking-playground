import random
import threading
import socket

def game(conn):
    # gen random number 1- 100 (inclusive)
    # make the player guess it. 
    ran_num = random.randint(1, 100)
    print(ran_num)
    conn.send("Welcome to the game\nguess the number (1..100) :".encode())
    #user_number = int(input("guess the number (1..100) :"))

    while True:
        user_number = int(conn.recv(1024).decode())
        if ran_num < user_number:
            conn.send("Too High".encode())
        elif ran_num > user_number: 
            conn.send("Too Low".encode())
        else:
            conn.send("Guessed".encode())
            break
    conn.close()

def handle_client(conn, addr):
    print(f"Connection established with {addr}")
    game(conn)

if __name__ == "__main__":
    host = '127.0.0.1'  # Localhost
    port = 12346        # Port number

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("Server is running and waiting for connections...")
    
    while True:
        conn, addr = server_socket.accept()
        
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

    handle_client()


