import matplotlib.pyplot as plt

def read_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    
    message_ids = []
    time_differences = []
    
    for line in lines:
        parts = line.split()
        message_id = int(parts[2])
        time_difference = float(parts[-2])
        message_ids.append(message_id)
        time_differences.append(time_difference)
    
    return message_ids, time_differences

def plot_graph(file1, file2, color1, color2, label1, label2, save_name):
    message_ids1, time_differences1 = read_file(file1)
    message_ids2, time_differences2 = read_file(file2)

    # Creating a new figure for each pair
    plt.figure()

    plt.plot(message_ids1, time_differences1, marker='o', label=label1, color=color1)
    plt.plot(message_ids2, time_differences2, marker='o', label=label2, color=color2)
    
    avg_time1 = sum(time_differences1) / len(time_differences1)
    avg_time2 = sum(time_differences2) / len(time_differences2)
    
    plt.axhline(avg_time1, linestyle='--', color=color1, label=f'Avg {label1}')
    plt.axhline(avg_time2, linestyle='--', color=color2, label=f'Avg {label2}')

    # Adding labels and title
    plt.xlabel('Message ID')
    plt.ylabel('Time Difference (seconds)')
    plt.title(f'Time Difference vs Message ID - {save_name}')

    # Adding legend
    plt.legend()

    # Decreasing the height of the graph
    plt.ylim(0, 0.008)

    # Marking all 25 points on the x-axis
    plt.xticks(range(1, 26))

    # Saving the plot
    plt.savefig(f'time_difference_graph_{save_name}.png')

    # Displaying the plot
    plt.show()

# File pairs
pair1 = ('http_message_size_10.txt', 'mqtt_qos2_message_size_10.txt', 'blue', 'green', 'HTTP Size 10', 'MQTT Size 10', 'pair1')
pair2 = ('http_message_size_20.txt', 'mqtt_qos2_message_size_20.txt', 'red', 'purple', 'HTTP Size 20', 'MQTT Size 20', 'pair2')
pair3 = ('http_message_size_40.txt', 'mqtt_qos2_message_size_40.txt', 'orange', 'brown', 'HTTP Size 40', 'MQTT Size 40', 'pair3')
pair4 = ('http_message_size_80.txt', 'mqtt_qos2_message_size_80.txt', 'blue', 'green', 'HTTP Size 80', 'MQTT Size 80', 'pair4')
pair5 = ('http_message_size_160.txt', 'mqtt_qos2_message_size_160.txt', 'orange', 'brown', 'HTTP Size 160', 'MQTT Size 160', 'pair5')

# Plotting the graphs for each pair
plot_graph(*pair1)
plot_graph(*pair2)
plot_graph(*pair3)
plot_graph(*pair4)
plot_graph(*pair5)

def read_connection_time(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    connection_times = {}

    for line in lines:
        parts = line.split()
        connection_type = parts[3]  # Assuming the connection type is at index 3 in the line
        connection_time = float(parts[-2])
        connection_times[connection_type] = connection_time

    return connection_times

def plot_connection_time(file_name, save_name):
    connection_times = read_connection_time(file_name)

    # Creating a new figure
    plt.figure()

    # Extracting connection types and times
    connection_types = list(connection_times.keys())
    times = list(connection_times.values())

    # Plotting two dots for different connection types
    plt.plot(connection_types, times, marker='o', linestyle='', color='blue', label='Connection Times')

    # Adding a horizontal dotted line through the dots
    for connection_type, time in zip(connection_types, times):
        plt.axhline(y=time, linestyle='--', color='green', alpha=0.5)

    # Bringing the types towards the center
    plt.xticks(connection_types)

    # Adding labels and title
    plt.xlabel('Connection Type')
    plt.ylabel('Connection Time (seconds)')
    plt.title(f'Connection Time - {save_name}')

    # Save the plot as a PNG
    plt.savefig('connection_time.png')

    # Displaying the plot
    plt.legend()
    plt.show()

# File pair for connection time
mqtt_connection_pair = ('connection_time.txt', 'mqtt_connection')

# Plotting the connection time graph and saving as PNG
plot_connection_time(*mqtt_connection_pair)
