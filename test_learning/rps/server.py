import threading
import socket
import random

rps = ['rock', 'paper', 'scissors']


def handle_client(connection):
    conn, addr = connection
    print(f'connected to {addr}')


    while True:
        conn.send("chose one from: 'rock', 'paper', 'scissors'".encode())
        user_choice = conn.recv(1024).decode()
        random_choice = random.choice(rps)

        print(f'user: {user_choice}')
        print(f'server: {random_choice}')

        if user_choice == random_choice:
            conn.send('Tie\n\n'.encode())
        else:
            if user_choice == 'rock' and random_choice == 'scissors':
                conn.send('Win\n\n'.encode())
            elif user_choice =='rock' and random_choice == 'paper':
                conn.send('Lose\n\n'.encode())
            elif user_choice =='paper' and random_choice == 'rock':
                conn.send('Win\n\n'.encode())
            elif user_choice =='paper' and random_choice == 'scissors':
                conn.send('Lose\n\n'.encode())
            elif user_choice =='scissors' and random_choice == 'rock':
                conn.send('Lose\n\n'.encode())
            elif user_choice =='scissors' and random_choice == 'paper':
                conn.send('Win\n\n'.encode())


if __name__ == "__main__":

    host = '127.0.0.1'
    port = 5005
    connection = (host, port)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(connection)
    server_socket.listen(5)

    print('Server is running!')

    while 1:
        connection = server_socket.accept()
        client_thread = threading.Thread(target = handle_client, args = (connection,))
        client_thread.start()
