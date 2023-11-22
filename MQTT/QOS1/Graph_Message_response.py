import pandas as pd
import matplotlib.pyplot as plt

# Load CSV files into DataFrames
http_data = pd.read_csv('http_response_times.csv')
mqtt_data = pd.read_csv('mqtt_response_times.csv')

# Select a specific payload size (e.g., 10 bytes)
payload_size = 10

# Filter data for the selected payload size
http_10_bytes = http_data[http_data['Payload Size (bytes)'] == payload_size].reset_index(drop=True)
mqtt_10_bytes = mqtt_data[mqtt_data['Payload Size (bytes)'] == payload_size].reset_index(drop=True)

# Plotting
plt.figure(figsize=(10, 6))

# Scatter plot for HTTP response times
plt.scatter(http_10_bytes.index + 1, http_10_bytes['HTTP Response Time (ms)'], color='darkblue', label='HTTP', marker='o', alpha=0.5)

# Scatter plot for MQTT response times
plt.scatter(mqtt_10_bytes.index + 1, mqtt_10_bytes['MQTT Response Time (ms)'], color='red', label='MQTT', marker='o', alpha=0.5)

# Connect data points with lines
plt.plot(http_10_bytes.index + 1, http_10_bytes['HTTP Response Time (ms)'], color='darkblue', linestyle='-', alpha=0.5)
plt.plot(mqtt_10_bytes.index + 1, mqtt_10_bytes['MQTT Response Time (ms)'], color='red', linestyle='-', alpha=0.5)

# Add labels and title
plt.xlabel('Message Number')
plt.ylabel('Response Time (ms)')
plt.title(f'HTTP vs MQTT Response Times for Payload Size {payload_size} bytes')
plt.legend()

# Save the plot as a PNG file
plt.savefig(f'response_times_message_number_10_bytes_darkblue_darkorange.png')

# Show the plot
plt.show()
