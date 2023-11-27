import asyncio
from aiocoap import Context, Message, Code
from aiocoap.resource import Resource

class MyResource(Resource):
    async def render_get(self, request):
        # Simulate server processing
        response_payload = b"Hello, CoAP Client!"

        # Define a request object based on the incoming request
        request_object = request

        # Your processing logic here, e.g., handling message sizes
        message_sizes = [10, 20, 40, 80, 160]
        remaining_message_sizes = set(message_sizes)

        for message_size in remaining_message_sizes.copy():
            if f'Message_Size_{message_size}' in request_object.uri_path:
                remaining_message_sizes.remove(message_size)

        # Send the response in blocks
        block_size = 32  # Set your preferred block size
        payload = response_payload
        while payload:
            block, payload = payload[:block_size], payload[block_size:]
            response = Message(code=Code.CONTENT, payload=block)
            response.opt.block1 = (0, True, block_size)  # Indicate block-wise transfer
            request.respond(response)

# Create CoAP server context
context = asyncio.get_event_loop().run_until_complete(Context.create_server_context(MyResource(), bind=('localhost', 5683)))

try:
    # Keep the server running
    asyncio.get_event_loop().run_forever()
except KeyboardInterrupt:
    print("Server shutting down...")
finally:
    # Clean up resources
    context.shutdown()
