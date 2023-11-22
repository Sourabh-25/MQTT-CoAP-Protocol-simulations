import paho.mqtt.client as mqtt
import time
import matplotlib.pyplot as plt

# Define MQTT broker settings
broker_address = "localhost"  # Change to the address of your MQTT broker
port = 1883
pub_topic = "example/test"  # Topic for sending test messages
ack_topic = "example/acknowledgment"  # Topic for receiving acknowledgments
qos = 2

# Define test parameters
message_sizes = [10, 20,40,80,160]  # Varying message sizes in bytes
message_frequencies = [5]  # Varying message frequencies in messages per second
quantities = [25]  # Number of messages to send for each scenario

# Function to generate a random message consisting of "X" characters
def generate_random_message(size):
    return "X" * size

# Create an MQTT client
client = mqtt.Client("test_publisher")

# Record the start time for MQTT connection establishment
mqtt_connect_start_time = time.time()

# Connect to the MQTT broker
client.connect(broker_address, port)

# Record the end time for MQTT connection establishment
mqtt_connect_end_time = time.time()

# Calculate and print the MQTT connection establishment time
mqtt_connection_time = mqtt_connect_end_time - mqtt_connect_start_time
print(f"Connected to MQTT broker")
print(f"MQTT Connection Establishment Time: {mqtt_connection_time:.8f} seconds")

sub_time_s = time.time()
# Subscribe to the acknowledgment topic
client.subscribe(ack_topic,qos=qos)
print(f"subscribed to topic: {ack_topic}")

sub_time_e = time.time()
sub_duration = sub_time_e-sub_time_s
print(f"MQTT Subscribtion Time: {sub_duration:.8f} seconds")

# Save the sum of mqtt_connection_time and sub_duration to connection_time.txt
total_connection_time = mqtt_connection_time + sub_duration
with open("connection_time.txt", "w") as conn_file:
    conn_file.write(f"Total Connection Time MQTT QOS2: {total_connection_time:.8f} seconds\n")


global_send_time_first=time.time()
# Initialize dictionaries to store data for different message sizes
message_data = {size: [] for size in message_sizes}

# ... (your existing code)

# Callback when an acknowledgment message is received
def on_ack_message(client, userdata, message):
    received_time = time.time()
    message_content = message.payload.decode()  # Extract the message content
    parts = message_content.split(' ')
    send_time = float(parts[0])
    msg_id = parts[1]
    time_difference_ack = received_time - send_time
    time_difference_msg = send_time - global_send_time_first

    # Store the message ID and time difference in the list
    size = int(parts[2])  # Extract the message size from the message content
    message_data[size].append((msg_id, time_difference_msg))

    print(f"Message sent at {global_send_time_first:.8f} was received by Subscriber at {send_time:.8f}")
    print(f"Acknowledgment received for message {msg_id} at {received_time:.8f}")
    print(f"Message sent in: {time_difference_msg:.8f} seconds")
    print(f"Ack received in: {time_difference_ack:.8f} seconds")

# Set the acknowledgment message callback
client.message_callback_add(ack_topic, on_ack_message)


client.loop_start()

try:
    for size in message_sizes:
        message_id = 0
        for frequency in message_frequencies:
            for quantity in quantities:
                for _ in range(quantity):
                    message_id += 1  # Increment the message ID
                    message = generate_random_message(size)
                    message_with_id = f"{message_id:04d} {message}"  # Include only message ID
                    send_start_time = time.time()
                    global_send_time_first = send_start_time
                    client.publish(pub_topic, message_with_id, qos=qos)
                    send_end_time = time.time()
                    send_duration = send_end_time - send_start_time
                    print(f"Scenario: {{'message_size': {size}, 'frequency': {frequency}, 'quantity': {quantity}}}, Published message {message_id} in: {send_duration:.8f} seconds")

                    time.sleep(1 / frequency)  # Adjust message sending frequency
except KeyboardInterrupt:
    pass

# Disconnect from the broker
client.loop_stop()
client.disconnect()


# Save data to text files for each message size
for size, data in message_data.items():
    filename = f"mqtt_qos2_message_size_{size}.txt"
    with open(filename, "w") as file:
        for msg_id, time_difference_msg in data:
            file.write(f"Message ID: {msg_id} Time Difference: {time_difference_msg:.8f} seconds\n")
