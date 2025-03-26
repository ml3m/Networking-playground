import socket
import random
import threading

# List of words to scramble
#WORD_LIST = ['house', 'car', 'phone', 'tablet', 'laptop', 'python', 'server', 'client', 'network', 'coding']
WORD_LIST = ['house', 'car', 'phone']

def handle_client(conn, addr):

    print(f"Connection established with {addr}")
    
    word = random.choice(WORD_LIST)
    word_l = list(word)
    random.shuffle(word_l)
    scramble_word = ''.join(word_l)
    while word == scramble_word:
        random.shuffle(word_l)
        scramble_word = ''.join(word_l)
    
    conn.send(f"Scrambled word: {scramble_word}".encode())
    
    while True:
        guess = conn.recv(1024).decode()
        if not guess:
            break
        
        if guess.lower() == word.lower():
            conn.send("Correct!".encode())
            print(f"Client {addr} guessed the word correctly!")
            break
        else:
            conn.send("Incorrect, try again".encode())
    
    print(f"Closing connection with {addr}")
    conn.close()

def main():
    """Main function to start the server."""
    host = '127.0.0.1'  # Localhost
    port = 12345        # Port number
    
    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    
    print("Server is running and waiting for connections...")
    
    while True:
        conn, addr = server_socket.accept()
        
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

if __name__ == "__main__":
    main()
