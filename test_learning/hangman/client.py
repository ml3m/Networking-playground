import socket
BUFFER = 1024

def main():
    connection_details = ('127.0.0.1', 5005)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(connection_details)
    
    print("Connected!")
    
    try:
        while True:
            server_message = client_socket.recv(BUFFER).decode()
            print(server_message)
            
            if "_" in server_message or "Incorrect" in server_message:
                user_letter = input("Enter a letter: ").strip()
                
                if not user_letter.isalpha() or len(user_letter) != 1:
                    print("Invalid input! Please enter a single letter.")
                    
                client_socket.send(user_letter.encode())
            
            elif "Congrats" in server_message:
                print("You won the game!")
                break
            
            elif "Error" in server_message or "Disconnecting" in server_message:
                print("The server encountered an error or disconnected.")
                break

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()
