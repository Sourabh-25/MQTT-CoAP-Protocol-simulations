# coap_server_simulation.py

import asyncio
from aiocoap import Message, Context, Code
from aiocoap.resource import Resource

class CacheBlock:
    def __init__(self, block_size):
        self.valid = [False] * block_size
        self.tag = [None] * block_size
        self.data = [None] * block_size

class Cache:
    def __init__(self, num_sets, blocks_per_set, block_size):
        self.num_sets = num_sets
        self.blocks_per_set = blocks_per_set
        self.block_size = block_size
        self.cache = [CacheBlock(blocks_per_set) for _ in range(num_sets)]

    def read(self, address):
        block_offset = address % self.block_size
        set_index = (address // self.block_size) % self.num_sets
        tag = address // (self.block_size * self.num_sets)

        cache_set = self.cache[set_index]
        for i in range(self.blocks_per_set):
            if cache_set.valid[i] and cache_set.tag[i] == tag:
                return cache_set.data[i][block_offset]

        # Simulate fetching data from memory
        data = [f"Data at address {address} block offset {i}" for i in range(self.block_size)]
        index_to_replace = address % self.blocks_per_set
        cache_set.valid[index_to_replace] = True
        cache_set.tag[index_to_replace] = tag
        cache_set.data[index_to_replace] = data
        return data[block_offset]

# Example Cache setting:
cache = Cache(num_sets=128, blocks_per_set=128, block_size=256)


class MyResource(Resource):
    def __init__(self):
        super().__init__()
        self.cache = {}

    async def render_get(self, request):
        # Check if the response is already in the cache
        response_payload = b"Hello, CoAP Client!"
        response_payload=response_payload
        request_object = request
        if request_object.uri_path in self.cache:
            cached_response = self.cache[request_object.uri_path]
            print(f"Cache hit for {request_object.uri_path}")
            return cached_response 

        # Simulate server processing
        message_sizes = [50, 100, 150]
        remaining_message_sizes = set(message_sizes)

        for message_size in remaining_message_sizes.copy():
            if f'Message_Size_{message_size}' in request_object.uri_path:
                remaining_message_sizes.remove(message_size)
        response=Message(payload=response_payload)
        self.cache[request.uri_path] = response
        # Send the response
        return response

async def coap_server_simulation():
    # Create CoAP server context
    context = await Context.create_server_context(MyResource(), bind=('localhost', 5683))

    try:
        # Keep the server running
        await asyncio.Future()
    except asyncio.CancelledError:
        print("Server shutting down...")

# Run the CoAP server
try:
    asyncio.run(coap_server_simulation())
except KeyboardInterrupt:
    pass
# ..server