import socket
import threading
import random

BUFFER = 1024

words = ['cat', 'laptop', 'looola']

def handle_client(connection_details):
    conn, addr = connection_details
    print(f"Connected to {addr}")

    word = random.choice(words)
    guessable = ['_'] * len(word)

    conn.send(''.join(guessable).encode())

    while True:
        try:

            found_letter = False
            user_letter = conn.recv(BUFFER).decode().strip()

            for i in range(len(word)):
                if user_letter == word[i]:
                    guessable[i] = user_letter
                    found_letter = True

            if found_letter:
                conn.send(''.join(guessable).encode())
            else:
                conn.send("Incorrect\n".encode())

            if ''.join(guessable) == word:
                conn.send(f"Congrats! You guessed the word: {word}\n".encode())
                break

        except Exception as e:
            print(f"err: {addr}: {e}")
            conn.send("err...\n".encode())
            break

    conn.close()
    print(f"Connection with {addr} closed.")

if __name__ == "__main__":
    host = '127.0.0.1'
    port = 5005
    connection_details = (host, port)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(connection_details)
    server_socket.listen(5)

    print("Server is running and waiting for connections...")
    
    while True:
        connection_details = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(connection_details,))
        client_thread.start()
