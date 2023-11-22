import http.server
import socketserver

# Set the IP address and port for the server
host = "0.0.0.0"  # Listen on all available network interfaces
port = 8080

# Define a custom request handler to capture response times
class CustomRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        # You can process the post_data here or record response times
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

# Create the HTTP server
with socketserver.TCPServer((host, port), CustomRequestHandler) as httpd:
    print(f"Serving at {host}:{port}")
    httpd.serve_forever()
