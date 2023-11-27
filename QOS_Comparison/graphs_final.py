import matplotlib.pyplot as plt
import numpy as np

# List of file names for each QoS level
qos0_files = ['mqtt_qos0_message_size_10.txt', 'mqtt_qos0_message_size_100.txt', 'mqtt_qos0_message_size_1000.txt']
qos1_files = ['mqtt_qos1_message_size_10.txt', 'mqtt_qos1_message_size_100.txt', 'mqtt_qos1_message_size_1000.txt']
qos2_files = ['mqtt_qos2_message_size_10.txt', 'mqtt_qos2_message_size_100.txt', 'mqtt_qos2_message_size_1000.txt']

# Plot for each message size
for i in range(len(qos0_files)):
    # Extract size information from the file names
    size_info = qos0_files[i].split('_')[-1].split('.')[0]
    
    # Load data from each QoS level
    with open(qos0_files[i], 'r') as file:
        lines0 = file.readlines()
        time_differences0 = [float(line.split()[-2]) for line in lines0 if 'Time Difference' in line]

    with open(qos1_files[i], 'r') as file:
        lines1 = file.readlines()
        time_differences1 = [float(line.split()[-2]) for line in lines1 if 'Time Difference' in line]

    with open(qos2_files[i], 'r') as file:
        lines2 = file.readlines()
        time_differences2 = [float(line.split()[-2]) for line in lines2 if 'Time Difference' in line]

    # Plot time differences against the x-axis for each QoS level
    plt.figure()
    plt.plot(range(len(time_differences0)), time_differences0, label=f'qos0_size_{size_info}')
    plt.plot(range(len(time_differences1)), time_differences1, label=f'qos1_size_{size_info}')
    plt.plot(range(len(time_differences2)), time_differences2, label=f'qos2_size_{size_info}')

    # Add labels and title
    plt.xlabel('Message Index')
    plt.ylabel('Time Differences (seconds)')
    plt.title(f'Time Differences for Message Size {size_info}')

    # Show legend
    plt.legend()

    # Show or save the plot
    plt.show()
