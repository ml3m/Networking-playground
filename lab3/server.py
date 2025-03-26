import socket
import threading

HOST = '127.0.0.1'
PORT = 5005

clients = []

def handle_client(conn, addr):
    print(f"New connection from {addr}")
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"Received from {addr}: {data}")
            broadcast(data, conn)
        except:
            break
    conn.close()
    if conn in clients:
        clients.remove(conn)
    print(f"Connection closed: {addr}")

def broadcast(message, sender_conn):
    for client in clients:
        if client != sender_conn:
            try:
                client.send(message.encode())
            except:
                if client in clients:
                    clients.remove(client)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Server started on {HOST}:{PORT}")
    try:
        while True:
            conn, addr = server.accept()
            clients.append(conn)
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
    except:
        print("\nShutting down server...")
        broadcast("Server is shutting down.")
        for client in clients:
            client.close()
        server.close()
        print("Server closed.")

if __name__ == "__main__":
    start_server()
