import paho.mqtt.client as mqtt
import time

# Define MQTT broker settings
broker_address = "localhost"  # Change to the address of your MQTT broker
port = 1883
pub_topic = "example/test"  # Topic for receiving test messages
ack_topic = "example/acknowledgment"  # Topic for sending acknowledgments
qos=2
# Create an MQTT client
client = mqtt.Client("subscriber")
# Create an MQTT client
client = mqtt.Client("subscriber")

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

# Subscribe to the test message topic
client.subscribe(pub_topic,qos=qos)
print(f"subscribed to topic: {pub_topic}")

sub_time_e = time.time()
sub_duration = sub_time_e-sub_time_s
print(f"MQTT Subscribtion Time: {sub_duration:.4f} seconds")

# Callback when a test message is received
def on_test_message(client, userdata, message):
    received_time = time.time()
    message_content = message.payload.decode()  # Extract the message content
    parts = message_content.split(' ')
    message_id = int(parts[0])  # Extract the message ID
    message_size = len(parts[1])
    
    print(f"Received test message {message_id} (Size: {message_size} bytes): {parts[1][:20]}... (Received at {received_time:.8f})")
    
    # Send an acknowledgment for the received message along with the send and receive times
    ack_send_time = time.time()
    ack_message = f"{received_time:.8f} {message_id} {message_size}"
    client.publish(ack_topic, ack_message, qos=qos)
    print(f"Acknowledgment sent for message {message_id} at {ack_send_time:.8f}")

# Set the test message callback
client.message_callback_add(pub_topic, on_test_message)

client.loop_start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass

# Disconnect from the broker
client.loop_stop()
client.disconnect()
