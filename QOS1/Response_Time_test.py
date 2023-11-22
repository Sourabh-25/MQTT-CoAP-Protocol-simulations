import paho.mqtt.client as mqtt
import requests
import time
import csv  # Import the csv module

# Define the MQTT broker's address and port
mqtt_broker_address = "localhost"
mqtt_broker_port = 1883

# Define the HTTP server's address and port
http_host = "localhost"
http_port = 8080
http_url = f"http://{http_host}:{http_port}"

# Define the topic to which you want to publish and subscribe
mqtt_topic = "test_topic"

# Number of messages to send for MQTT
num_messages_mqtt = 50

# Number of HTTP requests to send
num_requests_http = 50

# Create an MQTT client
mqtt_client = mqtt.Client()

# Open a CSV file for logging MQTT response times
csv_file_mqtt = open("mqtt_response_times.csv", "w", newline="")
csv_writer_mqtt = csv.writer(csv_file_mqtt)

# Write header to the CSV file
csv_writer_mqtt.writerow(["Payload Size (bytes)", "Send Time (seconds)", "Receive Time (seconds)", "MQTT Response Time (ms)"])

# Dictionary to store MQTT send times
mqtt_send_times = {}

# Sizes of data to send
data_sizes = [10,20,40,80,160]

# Define the on_connect callback function for MQTT
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
    else:
        print(f"Connection failed with error code {rc}")

# Define the on_message callback function for MQTT
received_messages_mqtt = 0
def on_message(client, userdata, message):
    global received_messages_mqtt
    received_messages_mqtt += 1

    # Get the send time from the dictionary
    topic = message.topic
    send_time = mqtt_send_times[topic]

    # Calculate MQTT response time
    receive_time = time.time()
    response_time_ms = (receive_time - send_time) * 1000

    # Write MQTT response time to the CSV file
    payload_size = len(message.payload)
    csv_writer_mqtt.writerow([payload_size, send_time, receive_time, response_time_ms])
    csv_file_mqtt.flush()

# Set the on_connect and on_message callback functions for MQTT
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

# Connect to the MQTT broker
mqtt_client.connect(mqtt_broker_address, mqtt_broker_port)

# Start the MQTT client's network loop
mqtt_client.loop_start()

# Subscribe to the MQTT topic
mqtt_client.subscribe(mqtt_topic, qos=1)

# Open a CSV file for logging HTTP response times
csv_file_http = open("http_response_times.csv", "w", newline="")
csv_writer_http = csv.writer(csv_file_http)

# Write header to the CSV file
csv_writer_http.writerow(["Payload Size (bytes)", "Send Time (seconds)", "Receive Time (seconds)", "HTTP Response Time (ms)"])

# Loop to send MQTT messages and record HTTP response times
for i in range(max(num_messages_mqtt, num_requests_http)):
    if i < num_messages_mqtt:
        # For MQTT, record the send time before publishing with variable payload size
        send_time = time.time()
        payload_size = data_sizes[i % len(data_sizes)]  # Cycle through the sizes
        payload = 'X' * payload_size  # Use 'X' as a placeholder character, adjust as needed
        mqtt_send_times[mqtt_topic] = send_time  # Store send time in the dictionary
        mqtt_client.publish(mqtt_topic, payload, qos=1)

    if i < num_requests_http:
        # For HTTP, record the send time before making an HTTP request with variable payload size
        send_time_http = time.time()
        payload_size_http = data_sizes[i % len(data_sizes)]  # Cycle through the sizes
        payload_http = 'X' * payload_size_http  # Use 'X' as a placeholder character, adjust as needed
        response = requests.post(http_url, data=payload_http)
        receive_time_http = time.time()
        response_time_ms_http = (receive_time_http - send_time_http) * 1000

        # Write HTTP response time to the CSV file
        csv_writer_http.writerow([payload_size_http, send_time_http, receive_time_http, response_time_ms_http])
        csv_file_http.flush()

    time.sleep(1)  # Adjust sleep duration as needed

# Wait for all MQTT messages to be received
while received_messages_mqtt < num_messages_mqtt:
    time.sleep(1)

# Close CSV files
csv_file_mqtt.close()
csv_file_http.close()
