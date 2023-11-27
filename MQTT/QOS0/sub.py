import paho.mqtt.client as mqtt
import time
import random
import string
import matplotlib.pyplot as plt
# Define MQTT broker settings
broker_address = "localhost"  # Change to the address of your MQTT broker
port = 1883
pub_topic = "example/test"  # Topic for receiving test messages
ack_topic = "example/acknowledgment"  # Topic for sending acknowledgments

# Create an MQTT client
client = mqtt.Client("subscriber")

# Connect to the MQTT broker
client.connect(broker_address, port)

# Subscribe to the test message topic
client.subscribe(pub_topic)
# Callback when a test message is received
def on_test_message(client, userdata, message):
    received_time = time.time()
    payload_str = message.payload.decode()
    decimal_part_str = payload_str.split()[0]
    size_str=payload_str.split()[1]
    send_time=float(decimal_part_str) 
    print(f"Received test message of size {size_str}:Sent at {decimal_part_str} (Received at {received_time:.8f})")
    time_difference = received_time - send_time
    print(f"Time difference: {time_difference:.8f} seconds")
    final_message=f"{send_time} {received_time}"
    # Send an acknowledgment for the received message
    client.publish(ack_topic, str(final_message), qos=0)
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
