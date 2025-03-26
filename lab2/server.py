#!/usr/bin/env python
import socket
import threading

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

# Function to handle communication with a single client
def handle_client(conn, addr, client_name):
    print "Client '{}' connected from address: {}".format(client_name, addr)
    try:
        while True:
            # Receive data from the client
            data = conn.recv(BUFFER_SIZE)
            if not data:
                print "Client '{}' disconnected.".format(client_name)
                break
            print "Received from {}: {}".format(client_name, data)
            
            # Echo the data back to the client
            conn.send("Server received: {}".format(data))
    except Exception as e:
        print "Error with client '{}': {}".format(client_name, e)
    finally:
        conn.close()
        print "Connection with '{}' closed.".format(client_name)

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and port
server_socket.bind((TCP_IP, TCP_PORT))

# Listen for incoming connections
server_socket.listen(5)  # Allow up to 5 queued connections
print "Server is listening on {}:{}".format(TCP_IP, TCP_PORT)

# Main loop to accept and handle multiple clients
client_count = 0
while True:
    conn, addr = server_socket.accept()
    client_count += 1
    client_name = "Client{}".format(client_count)  # Assign a unique name to each client
    
    # Start a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(conn, addr, client_name))
    client_thread.start()
