# coap_server_simulation.py

import asyncio
from aiocoap import Message, Context, Code
from aiocoap.resource import Resource

class MyResource(Resource):
    async def render_get(self, request):
        # Simulate server processing
        response_payload = b"Hello, CoAP Client!"

        # Define a request object based on the incoming request
        request_object = request

        # Our processing logic here, e.g., handling message sizes
        message_sizes = [50,100,150]
        remaining_message_sizes = set(message_sizes)

        for message_size in remaining_message_sizes.copy():
            if f'Message_Size_{message_size}' in request_object.uri_path:
                remaining_message_sizes.remove(message_size)

        # Send the response
        return Message(payload=response_payload)

async def coap_server_simulation():
    # Create CoAP server context
    context = await Context.create_server_context(MyResource(), bind=('localhost', 5683))

    try:
        while True:
            await asyncio.sleep(5)  # Adjust the sleep interval as needed
    except asyncio.CancelledError:
        print("Server shutting down...")

# Run the CoAP server
try:
    asyncio.run(coap_server_simulation())
except KeyboardInterrupt:
    pass
# ..server