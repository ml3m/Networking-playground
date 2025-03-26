import socket
import threading
import random


def handle_client(conn, addr):
    print(f"Connected to {addr}")
    
    # Generate a random list of integers
    original_list = [random.randint(0, 50) for _ in range(5)]
    shuffled_list = original_list[:]
    random.shuffle(shuffled_list)
    
    print(f"Original list: {original_list}")
    print(f"Shuffled list: {shuffled_list}")
    
    # Send the original list to the client
    conn.send(f"This is the list: {original_list}\n".encode())
    conn.send("Guess the order (comma-separated integers):\n".encode())
    
    while True:
        try:
            # Receive the user's guess
            user_guess = conn.recv(1024).decode().strip()
            if not user_guess:
                break
            
            # Convert the user's guess into a list of integers
            user_list_try = list(map(int, user_guess.split(',')))
            
            # Check if the guess matches the shuffled list
            if user_list_try == shuffled_list:
                conn.send("Congrats".encode())
                break
            else:
                conn.send("Incorrect. Try again.\n".encode())
        except Exception as e:
            conn.send(f"Error: {e}\n".encode())
            break
    
    conn.close()
    print(f"Connection with {addr} closed.")


if __name__ == "__main__":
    host = '127.0.0.1'  # Localhost
    port = 12346        # Port number

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("Server is running and waiting for connections...")
    
    while True:
        conn, addr = server_socket.accept()
        
        # Create a new thread for each client
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()
