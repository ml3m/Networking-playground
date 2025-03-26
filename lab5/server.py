import socket
import threading
import random

def handle_client(connection_details):
    conn, addr = connection_details  # Unpack the tuple
    print(f"Connected to {addr}")

    #In this game, the user has to guess the correct order of 5 random
    #computer-generated integers from a list of integers between 1 and 50.
    #
    
    original_list = [random.randint(0, 50) for _ in range(5)]
    shuffled_list = original_list[:]
    random.shuffle(shuffled_list)
    
    print(f"Original list: {original_list}")
    print(f"Shuffled list: {shuffled_list}")
    
    conn.send(f"This is the list: {original_list}\n".encode())
    conn.send("Guess the order (comma-separated integers):\n".encode())
    
    while True:
        try:
            # recieved the data from the client which is a string of type
            # "number,number,number" (in CSV format)

            user_guess = conn.recv(1024).decode().strip()
            if not user_guess:
                break
            
            # convertsion of the CSV format to the list.
            user_list_try = list(map(int, user_guess.split(',')))
            
            if user_list_try == shuffled_list:
                conn.send("Congrats! You guessed the order.\n".encode())
                break
            else:
                conn.send("Incorrect. Try again.\n".encode())
        except Exception as e:
            conn.send(f"Error: {e}\n".encode())
            break
    
    conn.close()
    print(f"conn with {addr} closed.")


if __name__ == "__main__":
    host = '127.0.0.1'
    port = 12346
    connection_details = (host, port)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(connection_details)
    server_socket.listen(5)

    print("Server is running and waiting for connections...")
    
    while True:
        connection_details = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(connection_details,))
        client_thread.start()
