import threading
import socket
import random

rps = ['rock', 'paper', 'scissors']

def handle_client(connection):
    conn, addr = connection
    print(f'Connected to {addr}')

    try:
        while True:
            random_choice = random.choice(rps)
            conn.send(f"What is the length of the word '{random_choice}'?".encode())

            while True:
                user_choice_len = conn.recv(1024).decode()

                if not user_choice_len.isdigit():
                    conn.send("Please enter a valid number.".encode())
                    continue

                user_choice_len = int(user_choice_len)

                if user_choice_len == len(random_choice):
                    conn.send("correct!".encode())
                    break
                else:
                    conn.send("incorect. Try again.".encode())

    except Exception as e:
        print(f"Error with client {addr}: {e}")
    finally:
        conn.close()
        print(f"Connection with {addr} closed.")

if __name__ == "__main__":
    host = '127.0.0.1'
    port = 5005
    connection = (host, port)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(connection)
    server_socket.listen(5)

    print('Server is running!')

    while True:
        connection = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(connection,))
        client_thread.start()
