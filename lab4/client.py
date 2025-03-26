import socket

def main():
    """Main function to start the client."""
    host = '127.0.0.1'  # Server's IP address
    port = 12345        # Server's port number
    
    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    print("Connected to the server!")
    
    while True:
        # Receive the scrambled word or response from the server
        server_message = client_socket.recv(1024).decode()
        print(server_message)
        
        # If the server says "Correct!", end the game
        if server_message == "Correct!":
            print("You guessed the word correctly! Game over.")
            break
        
        # Prompt the user for a guess
        guess = input("Enter your guess: ")
        client_socket.send(guess.encode())
    
    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    main()
