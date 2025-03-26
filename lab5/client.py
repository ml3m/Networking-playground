import socket

def main():
    connection_details = ('127.0.0.1', 12346)
    
    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(connection_details)
    
    print("Connected to the server!")
    
    try:
        
        while True:

            server_message = client_socket.recv(1024).decode()
            
            print(server_message)

            # iff the server prompts for a guess, send the user's input
            if "Guess the order" in server_message or "Incorrect. Try again." in server_message:
                user_guess = input("Enter your guess (csv format ex: 1,2,3,4,5): ")
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
        client_socket.close()
        print("Connection closed.")
    
    client_socket.close()

if __name__ == "__main__":
    main()
