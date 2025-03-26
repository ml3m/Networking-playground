#!/usr/bin/env python
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((TCP_IP, TCP_PORT))
print "Connected to the server at {}:{}".format(TCP_IP, TCP_PORT)

try:
    # Send a name to the server
    client_name = raw_input("Enter your name: ")
    client_socket.send(client_name)
    
    while True:
        # Get user input
        MESSAGE = raw_input("Enter message to send (type 'exit' to quit): ")
        
        # Exit the loop if the user types 'exit'
        if MESSAGE.lower() == 'exit':
            print "Closing connection..."
            break
        
        # Send the message to the server
        client_socket.send(MESSAGE)
        
        # Receive the response from the server
        data = client_socket.recv(BUFFER_SIZE)
        print "Received from server:", data
finally:
    # Close the connection
    client_socket.close()
    print "Connection closed."
