import time
import pickle

# Define data for serialization
data = {
    "name": "John Doe",
    "age": 30,
    "email": "johndoe@example.com",
    "address": "123 Main St",
    "city": "Anytown",
}

# Number of iterations to measure serialization/deserialization overhead
iterations = 1000

def measure_serialization_deserialization_overhead(data, iterations):
    serialization_times = []
    deserialization_times = []

    for _ in range(iterations):
        # Serialize the data
        start_time = time.time()
        serialized_data = pickle.dumps(data)
        end_time = time.time()
        serialization_times.append(end_time - start_time)

        # Deserialize the data
        start_time = time.time()
        deserialized_data = pickle.loads(serialized_data)
        end_time = time.time()
        deserialization_times.append(end_time - start_time)

    avg_serialization_time = sum(serialization_times) / len(serialization_times)
    avg_deserialization_time = sum(deserialization_times) / len(deserialization_times)

    return avg_serialization_time, avg_deserialization_time

avg_serialization_time, avg_deserialization_time = measure_serialization_deserialization_overhead(data, iterations)
    
print(f"Average Serialization Time: {avg_serialization_time:.6f} seconds")
print(f"Average Deserialization Time: {avg_deserialization_time:.6f} seconds")
