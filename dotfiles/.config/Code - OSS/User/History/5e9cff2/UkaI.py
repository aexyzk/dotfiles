import socket
import threading

HOST="0.0.0.0"
PORT=3621

####################################################

import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 12345
ADDRESS = (HOST, PORT)

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind(ADDRESS)

# Listen for incoming connections
server_socket.listen()

# List to store connected clients
clients = []

# Function to broadcast messages to all clients
def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except Exception as e:
            print(f"Error broadcasting to a client: {e}")

# Function to handle a client connection
def handle_client(client_socket, client_address):
    print(f"Connection from {client_address}")

    # Add the client to the list
    clients.append(client_socket)

    try:
        while True:
            # This server sends a message to all clients every 5 seconds
            message = "Hello from the server!"
            broadcast(message.encode())
            # Sleep for 5 seconds before sending the next message
            threading.Event().wait(5)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Remove the client from the list and close the connection
        clients.remove(client_socket)
        client_socket.close()
        print(f"Connection from {client_address} closed")

# Accept and handle incoming connections
print(f"Server listening on {HOST}:{PORT}")
while True:
    client_socket, client_address = server_socket.accept()
    client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_handler.start()
