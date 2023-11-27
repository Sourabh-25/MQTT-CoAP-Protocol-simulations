import matplotlib.pyplot as plt
import numpy as np

# List of file names for each QoS level
qos2_files = ['mqtt_qos2_message_size_10.txt', 'mqtt_qos2_message_size_100.txt', 'mqtt_qos2_message_size_1000.txt']

# Plot for each QoS level
for qos_file in qos2_files:
    # Extract QoS level and size information from the file name
    qos_level = qos_file.split('_')[2][3:]
    size_info = qos_file.split('_')[-1].split('.')[0]
    
    # Load data from the file
    with open(qos_file, 'r') as file:
        lines = file.readlines()
        time_differences = [float(line.split()[-2]) for line in lines if 'Time Difference' in line]

    # Plot time differences against the x-axis
    plt.plot(range(len(time_differences)), time_differences, label=f'qos2_size_{size_info}')

# Add labels and title
plt.xlabel('Message Index')
plt.ylabel('Time Differences (seconds)')
plt.title(f'Time Differences for QoS Levels')

# Show legend
plt.legend()

# Show or save the plot
plt.show()
