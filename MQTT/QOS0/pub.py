import paho.mqtt.client as mqtt
import time
import random
import string
import matplotlib.pyplot as plt

# Define MQTT broker settings
broker_address = "localhost"  # Change to the address of your MQTT broker
port = 1883
pub_topic = "example/test"  # Topic for sending test messages
ack_topic = "example/acknowledgment"  # Topic for receiving acknowledgments

# Define test parameters
message_sizes = [10,20,40,80,160]  # Varying message sizes in bytes
message_frequencies = [5]  # Varying message frequencies in messages per second
# Function to generate a random message of a specified size
def generate_random_message(size):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))

# Function to plot the message receive times
def plot_receive_times(receive_times):
    plt.plot(receive_times, marker='o', linestyle='-')
    plt.xlabel("Message Index")
    plt.ylabel("Time (seconds)")
    plt.title("Message Receive Times")
    plt.grid()
    plt.show()

# Create an MQTT client
client = mqtt.Client("test_publisher")

for size in message_sizes:
    # Lists to store message times
    send_times = []
    receive_times = []
    file_path = f"message_details_size_{size}.txt"
    with open(file_path, "w") as file:
        file.write("Message Details:\n")

    # Function to write message details to the file
    def write_message_details(message_id, time_difference):
        with open(file_path, "a") as file:
            file.write(f"Message ID: {message_id} Time Difference: {time_difference:.8f} seconds\n")
    # Connect to the MQTT broker
    client.connect(broker_address, port)

    # Subscribe to the acknowledgment topic
    client.subscribe(ack_topic)

    # Callback when an acknowledgment message is received
    def on_ack_message(client, userdata, message):
        payload_str = message.payload.decode()
        send_time = float(payload_str.split()[0])
        received_time=float(payload_str.split()[1])
        send_times.append(send_time)
        receive_times.append(received_time)
        time_difference = received_time - send_time
        message_id = len(receive_times)
        print(f"Message sent at {send_time:.8f} was received by Subscriber at {received_time:.8f}")
        print(f"Time difference: {time_difference:.8f} seconds")
        # Write message details to the file
        write_message_details(message_id, time_difference)
    # Set the acknowledgment message callback
    client.message_callback_add(ack_topic, on_ack_message)
    client.loop_start()
    try:
        messages_sent = 0  # Counter for the number of messages sent
        while messages_sent < 25:
            for frequency in message_frequencies:
                message = generate_random_message(size)
                # Record the timestamp when the message is sent
                send_time = time.time()
                message_with_time = f"{send_time:.8f} {size} {message}"  # Include send time in the message
                print(f"Publishing message with size {size} and frequency {frequency} Hz")
                # Publish the message with QoS 0 (At most once)
                client.publish(pub_topic, message_with_time, qos=0)
                time.sleep(1 / frequency)  # Adjust message sending frequency
                messages_sent += 1
    except KeyboardInterrupt:
        pass
    # Disconnect from the broker
    client.loop_stop()
    client.disconnect()
    message_ids = list(range(1, len(receive_times) + 1))
    time_differences = [received - send for send, received in zip(send_times, receive_times)]
    plt.figure()
    plt.plot(message_ids, time_differences, marker='o', linestyle='-')
    plt.xlabel("Message Index")
    plt.ylabel("Time Difference (seconds)")
    plt.title(f"Message Index vs Time Difference (Size {size})")
    plt.grid()
    plt.show()
