import socket

def start_client(server_host, server_port):
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to the server
        client_socket.connect((server_host, server_port))
        print(f'Connected to server at {server_host}:{server_port}')
        
        while True:
            # Send a message to the server
            message = input('Enter message to send to server: ')
            if message.lower() == 'exit':
                break
            client_socket.send(message.encode())
            
            # Receive a response from the server
            response = client_socket.recv(1024).decode()
            print(f'Response from server: {response}')
    
    except ConnectionError:
        print('Failed to connect to the server')
    
    finally:
        # Close the client socket
        client_socket.close()
        print('Connection closed')

if __name__ == '__main__':
    server_host = 'localhost'  # Change this to the server's host address if necessary
    server_port = 12345        # Ensure this matches the server's listening port
    start_client(server_host, server_port)
