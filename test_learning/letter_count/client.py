import socket

def main():

    host = '127.0.0.1'
    port = 5005
    connection = (host, port)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(connection)

    print('connected')

    server_message = server_socket.recv(1024).decode()
    print(server_message)

    while True:
        user_choice = input()

        server_socket.send(user_choice.encode())
        response_server = server_socket.recv(1024).decode()
        if 'correct!' in response_server:
            print(response_server)
            print('game finished\n')
            break
        else:
            print(response_server)
            print('try again.\n')


    server_socket.close()

    

if __name__ == "__main__":
    main()
