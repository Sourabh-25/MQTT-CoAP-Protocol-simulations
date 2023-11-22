import socket
import time

# Server settings
server_host = "localhost"
server_port = 8080

# Number of iterations to measure connection overhead
iterations = 10

def measure_connection_overhead():
    connection_times = []

    for _ in range(iterations):
        start_time = time.time()
        try:
            with socket.create_connection((server_host, server_port)) as sock:
                end_time = time.time()
        except ConnectionRefusedError:
            print("Error: Connection to the server was refused. Make sure the server is running.")
            return

        connection_time = end_time - start_time
        connection_times.append(connection_time)

    return connection_times

connection_times = measure_connection_overhead()

if not connection_times:
    # The function returned early due to a connection error
    exit(1)

avg_connection_time = sum(connection_times) / len(connection_times)
print(f"Average connection time: {avg_connection_time:.8f} seconds")

# Append the avg_connection_time to connection_time.txt
total_connection_time = avg_connection_time
with open("connection_time.txt", "a") as conn_file:
    conn_file.write(f"Total Connection Time HTTP: {total_connection_time:.8f} seconds\n")
