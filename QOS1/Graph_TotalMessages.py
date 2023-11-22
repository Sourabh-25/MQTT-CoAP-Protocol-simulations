import matplotlib.pyplot as plt

# Lists to store the total times MQTT and HTTP messages were sent for each data size
total_mqtt_messages = []
total_http_messages = []

# List of data sizes in bytes
data_sizes_bytes = [10, 20, 40, 80, 160]

# Parse the log files to calculate total times sent for each data size
for data_size in data_sizes_bytes:
    mqtt_count = 0
    http_count = 0

    with open(f"results_{data_size}.txt", "r") as log_file:
        lines = log_file.readlines()
        for line in lines:
            if "MQTT Data Size" in line:
                mqtt_count += 1
            elif "HTTP Data Size" in line:
                http_count += 1

    total_mqtt_messages.append(mqtt_count)
    total_http_messages.append(http_count)

# Create a line chart
plt.plot(data_sizes_bytes, total_mqtt_messages, marker='o', label="MQTT")
plt.plot(data_sizes_bytes, total_http_messages, marker='o', label="HTTP")

# Set labels and title
plt.xlabel('Data Size (bytes)')
plt.ylabel('Total Times Sent')
plt.title('Total Times MQTT and HTTP Messages Were Sent for sending 25 messages')

# Add a legend
plt.legend()

# Set y-ticks to include 25
plt.yticks(list(plt.yticks()[0]) + [25])

# Save the chart as a PNG file
plt.savefig('message_count.png')

# Show the chart
plt.show()
