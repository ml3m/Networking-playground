import socket
import threading
import sys

HOST = '127.0.0.1'
PORT = 5005

def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode()
            if not message:
                raise ConnectionError
            print("Message from server:", message)
        except:
            print("Server closed.")
            client.close()
            sys.exit()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((HOST, PORT))
    print("Connected to the server.")
except:
    print("Unable to connect to the server.")
    sys.exit()

thread = threading.Thread(target=receive_messages, args=(client,))
thread.start()

while True:
    try:
        message = input("You: ")
        client.send(message.encode())
    except:
        print("Connection lost. Exiting...")
        client.close()
        sys.exit()
