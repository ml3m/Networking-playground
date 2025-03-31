import socket

def main():

    host = '127.0.0.1'
    port = 5005
    connection = (host, port)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(connection)

    print('connected')

    while True:
        server_message = server_socket.recv(1024).decode()
        print(server_message)
        user_choice = input()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print('enter correct input from list: ')
        else:
            server_socket.send(user_choice.encode())


    server_socket.close()

    

if __name__ == "__main__":
    main()
