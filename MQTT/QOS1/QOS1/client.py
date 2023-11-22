import paho.mqtt.client as mqtt
import time

# Define the MQTT broker's address and port
broker_address = "localhost"
broker_port = 1883

# Define the topic to which you want to publish and subscribe
topic = "jay"

# Create an MQTT client
client = mqtt.Client()

# Define the on_connect callback function
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        # Subscribe to the topic when connected
        client.subscribe(topic)
    else:
        print(f"Connection failed with error code {rc}")

# Define the on_message callback function
def on_message(client, userdata, message):
    # Calculate response time by subtracting the send time from the current time
    receive_time = time.time()
    send_time = client.send_time
    response_time_us = (receive_time - send_time) * 1e6  # Convert to microseconds (µs)

    print(f"Received message on topic '{message.topic}' with response time: {response_time_us:.2f} microseconds")

# Set the on_connect and on_message callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

# Start the MQTT client's network loop
client.loop_start()

while True:
    message = input("Enter a message to publish (or 'exit' to quit): ")
    if message.lower() == "exit":
        break

    # Record the send time for the message
    client.send_time = time.time()
    client.publish(topic, message, qos=1)

# The client continues running, and you can publish more messages as needed

# To exit the client, you can use a KeyboardInterrupt (Ctrl+C) or another method
