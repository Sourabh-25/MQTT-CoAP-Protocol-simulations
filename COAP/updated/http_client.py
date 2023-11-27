import asyncio
import pandas as pd
import time
import aiohttp

async def http_client_simulation(nodes=5):
    # Define HTTP server details
    server_address = 'http://localhost:8080/Message_Size_{message_size}'

    # Simulate multiple nodes
    results = []
    total_time_start = time.time()  # Record the start time for total time calculation

    async with aiohttp.ClientSession() as session:
        for node in range(1, nodes + 1):
            # Simulate multiple message sizes
            for message_size in [10, 20, 40, 80, 160]:  # Adjust sizes based on your requirements
                # Construct HTTP request
                url = server_address.format(message_size=message_size)

                # Send the request and wait for the response
                try:
                    start_time = time.time()
                    async with session.get(url) as response:
                        content = await response.text()
                    end_time = time.time()

                    # Calculate latency and throughput
                    latency = end_time - start_time  # Seconds
                    throughput = message_size / latency  # Bytes per second

                    # Record metrics
                    results.append({
                        'Node': node,
                        'Message_Size': message_size,
                        'Latency': latency,
                        'Throughput': throughput
                    })

                    print(f'Response from server for Node {node}, Message Size {message_size}: {content}')
                except Exception as e:
                    print(f'Error: {e}')

    total_time_end = time.time()  # Record the end time for total time calculation

    # Save results to CSV
    results_df = pd.DataFrame(results)
    results_df['Total_Time'] = total_time_end - total_time_start  # Add a column for total time
    results_df.to_csv('http_client_results.csv', index=False)

# Run the HTTP client simulation with 5 nodes (you can adjust this number)
asyncio.run(http_client_simulation(nodes=5))
