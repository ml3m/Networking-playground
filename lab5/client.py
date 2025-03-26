import socket

def main():
    host = '127.0.0.1'  # Server's IP address
    port = 12346        # Server's port number
    
    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    print("Connected to the server!")
    
    try:
        while True:
            # Receive data from the server
            server_message = client_socket.recv(1024).decode()
            print(server_message)

            # If the server prompts for a guess, send the user's input
            if "Guess the order" in server_message or "Incorrect. Try again." in server_message:
                user_guess = input("Enter your guess (comma-separated integers): ")
                client_socket.send(user_guess.encode())
            elif "Congrats" in server_message:
                print("you found it!")
                break
            elif "Error" in server_message:
                print("error.")
                break
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection
        client_socket.close()
        print("Connection closed.")
    
    client_socket.close()

if __name__ == "__main__":
    main()
