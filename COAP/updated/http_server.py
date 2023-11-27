import asyncio
from aiohttp import web

async def handle(request):
    # Simulate server processing
    message_size = int(request.match_info['message_size'])
    response_payload = f"Hello, HTTP Client! Message Size: {message_size}".encode()

    # Simulate processing time
    await asyncio.sleep(1)

    return web.Response(body=response_payload)

async def http_server_simulation():
    app = web.Application()
    app.router.add_get('/Message_Size_{message_size}', handle)

    # Create HTTP server context
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()

    try:
        # Keep the server running
        await asyncio.Future()
    except asyncio.CancelledError:
        print("Server shutting down...")

# Run the HTTP server
try:
    asyncio.run(http_server_simulation())
except KeyboardInterrupt:
    pass
