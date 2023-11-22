import paho.mqtt.client as mqtt
import requests
import time
import random
import threading
import csv


# Define the MQTT broker's address and port
mqtt_broker_address = "localhost"
mqtt_broker_port = 1883

# Define the MQTT topic
mqtt_topic = "jay"

# Define the HTTP server's address and port
http_host = "localhost"
http_port = 8080
http_url = f"http://{http_host}:{http_port}"

# List of different data sizes to send
data_sizes_bytes = [10,20,40,80,160]

# Number of messages for each data size
num_messages = 25  # Increase the number of messages

# Create an MQTT client
mqtt_client = mqtt.Client()

# Define the on_publish callback for MQTT
def on_publish(client, userdata, mid):
    if mid in userdata:
        userdata[mid] += 1
    else:
        userdata[mid] = 1

mqtt_client._userdata = {}  # Initialize the user data for on_publish callback
mqtt_client.on_publish = on_publish

# Connect to the MQTT broker
mqtt_client.connect(mqtt_broker_address, mqtt_broker_port)

# Function to send MQTT message
def send_mqtt_message(data_size, result_file):
    successful_message_count_mqtt = 0
    while successful_message_count_mqtt < num_messages:
        result, mid = mqtt_client.publish(mqtt_topic, "X" * data_size, qos=1)
        # Process MQTT messages for up to 1 second
        mqtt_client.loop(timeout=1.0)
        if mid in mqtt_client._userdata:
            successful_message_count_mqtt += 1
        time.sleep(random.uniform(0, 1))
        result_file.write(f"MQTT Data Size: {data_size}, Successful Messages: {successful_message_count_mqtt}\n")

# Function to send HTTP request
def send_http_request(data_size, result_file):
    successful_message_count_http = 0
    for _ in range(num_messages):
        http_start_time = time.time()
        response = requests.get(http_url)
        http_end_time = time.time()
        if response.status_code == 200:
            successful_message_count_http += 1
        time.sleep(random.uniform(0, 1))
        result_file.write(f"HTTP Data Size: {data_size}, Successful Messages: {successful_message_count_http}\n")

# Create threads and result files for each data size
threads = []
result_files = []

for data_size in data_sizes_bytes:
    result_file = open(f"results_{data_size}.txt", "w")
    result_files.append(result_file)

    http_thread = threading.Thread(target=send_http_request, args=(data_size, result_file))
    threads.append(http_thread)

# Start all threads
for thread in threads:
    thread.start()

# Start sending MQTT messages in the main thread
for data_size in data_sizes_bytes:
    send_mqtt_message(data_size, result_files[data_sizes_bytes.index(data_size)])

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Close result files
for result_file in result_files:
    result_file.close()
# Disconnect from the MQTT broker
mqtt_client.disconnect()
