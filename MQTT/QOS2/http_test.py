import http.client
import time
import random
import matplotlib.pyplot as plt

# Server settings
server_host = "localhost"
server_port = 8001

# Define test scenarios
message_sizes = [10, 20,40,80,160]  # Varying message sizes in bytes
frequencies = [5]  # Varying frequencies in messages per second
quantities = 25  # Fixed quantity of messages to be sent

def send_request(message):
    conn = http.client.HTTPConnection(server_host, server_port)
    conn.request("GET", f"/?data={message}")
    start_send_time = time.time()
    response = conn.getresponse()
    end_send_time = time.time()

    # Check the HTTP response status code
    if response.status != 200:
        print(f"Error: Unexpected status code {response.status} for message: {message}")

    response_data = response.read().decode('utf-8')  # Read and decode the response data

    conn.close()
    return start_send_time, end_send_time, response_data

for message_size in message_sizes:
    # Create a text file for each message size
    with open(f'http_message_size_{message_size}.txt', 'w') as file:
        file.write("")

    for frequency in frequencies:
        for message_number in range(quantities):
            # Generate a random message of the specified size
            message = "".join(random.choices("X", k=message_size))

            # Measure the time taken to send the request
            send_start_time, send_end_time, response_data = send_request(message)

            # Calculate the request time
            request_time = send_end_time - send_start_time

            # Control the frequency of requests
            time.sleep(1 / frequency)

            response_start_time = time.time()
            response_time = response_start_time - send_end_time

            scenario = {
                "message_size": message_size,
                "frequency": frequency,
                "message_number": message_number
            }

            print(f"Scenario: {scenario}, Request Time: {request_time:.8f} seconds, Response Time: {response_time:.8f} seconds")

            # Save message number and request time to the text file
            with open(f'http_message_size_{message_size}.txt', 'a') as file:
                file.write(f"Message ID: {message_number+1} Time Difference: {request_time:.8f} seconds\n")


            # Check and handle response data, e.g., perform additional validation
            if message in response_data:
                print("Response data contains the expected value.")
            else:
                print("Response data does not contain the expected value.")
                # You can add more error-handling logic as needed
