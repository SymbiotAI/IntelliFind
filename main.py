import http.server
import socketserver
from src.openai_embeddings.request import make_http_call_with_chunking
import json
import os
# Define the port number to listen on
PORT = 8010

# Define the request handler class
class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Customize the response

        #This calls openai_embeddings/request.py function to do stuff.

        self.request

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, World!")
    def do_POST(self):

        self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        self.send_response(200)
        self.end_headers()

        data = json.loads(self.data_string)
        make_http_call_with_chunking(input_string=data.input, model=data.model, api_key=os.environ.get('EMBDEDDINGS_OPENAI_API_KEY'))
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Finished Indexing!")

# Create a TCP/IP socket server
with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"Server listening on port {PORT}")
    httpd.serve_forever()