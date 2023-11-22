import paho.mqtt.client as mqtt

# Define the MQTT broker's address and port
broker_address = "localhost"
broker_port = 1883

# Define the topic to subscribe to
topic = "jay"

# Create an MQTT client
client = mqtt.Client()

# Define the on_connect and on_message callback functions
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        client.subscribe(topic,qos=1)
    else:
        print(f"Connection failed with error code {rc}")

def on_message(client, userdata, message):
    print(f"Received message on topic '{message.topic}': {str(message.payload)}")

# Set the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
print("Connecting to MQTT broker...")
client.connect(broker_address, broker_port)

# Start the MQTT client's network loop
print("Starting MQTT loop...")
client.loop_forever()
