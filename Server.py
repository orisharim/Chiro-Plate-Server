import socket
import threading
class Server:
    
    def __init__(self, server_host, server_port):
        self.server_host = server_host
        self.server_port = server_port
    
    
    def handle_client(self, client_socket, client_address):
        print(f'Connection established with {client_address}')
        
        while True:
            # Receive data from the client
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f'Message from {client_address}: {message}')
            
            # Send a response back to the client
            response = 'Message received\n'
            client_socket.send(response.encode())
        
        # Close the client socket
        client_socket.close()
        print(f'Connection closed with {client_address}')

    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.server_host, self.server_port))
        server_socket.listen(5)

        print(f'Server is listening on {self.server_host}:{self.server_port}...')

        while True:
            client_socket, client_address = server_socket.accept()
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
            client_thread.start()
            print(f'Active connections: {threading.active_count() - 1}')
        
    
