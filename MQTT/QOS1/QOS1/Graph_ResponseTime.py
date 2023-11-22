import pandas as pd
import matplotlib.pyplot as plt

# Load CSV files into DataFrames
http_data = pd.read_csv('http_response_times.csv')
mqtt_data = pd.read_csv('mqtt_response_times.csv')

# Calculate average response times
avg_http_response = http_data.groupby('Payload Size (bytes)')['HTTP Response Time (ms)'].mean().reset_index()
avg_mqtt_response = mqtt_data.groupby('Payload Size (bytes)')['MQTT Response Time (ms)'].mean().reset_index()

# Plotting
plt.figure(figsize=(10, 6))

# Scatter plot for HTTP response times
plt.scatter(http_data['Payload Size (bytes)'], http_data['HTTP Response Time (ms)'], color='blue', label='HTTP', marker='o', alpha=0.5)

# Scatter plot for MQTT response times
plt.scatter(mqtt_data['Payload Size (bytes)'], mqtt_data['MQTT Response Time (ms)'], color='orange', label='MQTT', marker='o', alpha=0.5)

# Line plot with markers for average HTTP response times (using a different color)
plt.plot(avg_http_response['Payload Size (bytes)'], avg_http_response['HTTP Response Time (ms)'], marker='o', linestyle='-', color='green', label='Avg HTTP')

# Line plot with markers for average MQTT response times (using a different color)
plt.plot(avg_mqtt_response['Payload Size (bytes)'], avg_mqtt_response['MQTT Response Time (ms)'], marker='o', linestyle='-', color='red', label='Avg MQTT')

# Add labels and title
plt.xlabel('Payload Size (bytes)')
plt.ylabel('Response Time (ms)')
plt.title('HTTP vs MQTT Response Times')
plt.legend()

# Save the plot as a PNG file
plt.savefig('response_times_plot.png')

# Show the plot
plt.show()
