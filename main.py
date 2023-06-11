import http.server
import socketserver
from src.openai_embeddings.tst import indexText
import json
import os

# Define the port number to listen on
PORT = 8080


# Define the request handler class
class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, World!")

    def do_POST(self):
        data_string = self.rfile.read(int(self.headers['Content-Length']))

        # self.send_response(200)
        # self.end_headers()

        data = json.loads(data_string)
        indexText(data.input)
        # api_key=os.environ.get('EMBDEDDINGS_OPENAI_API_KEY')
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Finished Indexing!")
        self.send_response(200)


# Create a TCP/IP socket server
with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"Server listening on port {PORT}")
    httpd.serve_forever()
