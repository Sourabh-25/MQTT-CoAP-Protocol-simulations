import matplotlib.pyplot as plt
import numpy as np

# Function to extract time differences from a file
def extract_time(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        times = [float(line.split(" ")[-2]) for line in lines]
    return times

# List of file names
files = [
    "mqtt_qos2_message_size_10.txt",
    "mqtt_qos2_message_size_20.txt",
    "mqtt_qos2_message_size_40.txt",
    "mqtt_qos2_message_size_80.txt",
    "mqtt_qos2_message_size_160.txt"
]

# Extract time differences for each file
time_data = [extract_time(file) for file in files]

# Message sizes
message_sizes = [10, 20, 40, 80, 160]

# Plotting
fig, ax = plt.subplots()

# Plot individual points
for i, times in enumerate(time_data):
    ax.scatter([message_sizes[i]] * len(times), times, label=f'Message Size {message_sizes[i]}')

# Plot average points
avg_times = [np.mean(times) for times in time_data]
ax.scatter(message_sizes, avg_times, color='red', marker='x', label='Average')

# Connect the average points
ax.plot(message_sizes, avg_times, linestyle='--', color='red')

# Set labels and title
ax.set_xlabel('Message Size')
ax.set_ylabel('Time Difference (seconds)')
ax.set_title('Time Difference vs Message Size')

# Show legend
ax.legend()

plt.savefig('bw_msg_sizes.png')

# Show the plot
plt.show()
