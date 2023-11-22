import socket

# Server settings
server_host = "localhost"
server_port = 8080

# Number of iterations to measure connection overhead
iterations = 10

def start_server():
    # Create a socket and bind it to the server address
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((server_host, server_port))
        server_socket.listen(1)  # Listen for incoming connections
        print(f"Server is listening on {server_host}:{server_port}")

        while True:
            conn, addr = server_socket.accept()  # Accept a new connection
            with conn:
                # Connection established
                print(f"Connected by {addr}")

start_server()
