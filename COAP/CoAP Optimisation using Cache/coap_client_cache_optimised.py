# coap_client_simulation.py

import asyncio
import pandas as pd
import time
from aiocoap import Context, Message, Code

  
async def coap_client_simulation(nodes=5):
    # Define CoAP server details
    server_address = 'coap://localhost:5683/path/resource'

    # Simulate multiple nodes
    results = []
    total_time_start = time.time()  # Record the start time for total time calculation

    for node in range(1, nodes + 1):
        # Simulate multiple message sizes
        for message_size in [50, 100, 150]:  # Adjust sizes based on your requirements
            # Construct CoAP request
            request = Message(code=Code.GET, uri=server_address, payload=b'A' * message_size)

            # Create CoAP client context and request
            context = await Context.create_client_context()

            try:
                start_time = time.time()
                response = await context.request(request).response
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

                print(f'Response from server for Node {node}, Message Size {message_size}: {response.payload}')
            except Exception as e:
                print(f'Error: {e}')
            finally:
                await context.shutdown()

    total_time_end = time.time()  # Record the end time for total time calculation

    # Save results to CSV
    results_df = pd.DataFrame(results)
    results_df['Total_Time'] = total_time_end - total_time_start  # Add a column for total time
    results_df.to_csv('coap_cache_results.csv', index=False)

# Run the CoAP client simulation with 5 nodes (you can adjust this number)
asyncio.run(coap_client_simulation(nodes=5))