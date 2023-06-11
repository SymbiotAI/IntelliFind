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

    def do_PUT(self):
        """Save a file following a HTTP PUT request"""
        filename = os.path.basename(self.path)

        # Don't overwrite files
        if os.path.exists(filename):
            self.send_response(409, 'Conflict')
            self.end_headers()
            reply_body = '"%s" already exists\n' % filename
            self.wfile.write(reply_body.encode('utf-8'))
            return

        file_length = int(self.headers['Content-Length'])
        read = 0
        with open(filename, 'wb+') as output_file:
            while read < file_length:
                new_read = self.rfile.read(min(66556, file_length - read))
                read += len(new_read)
                output_file.write(new_read)
        self.send_response(201, 'Created')
        self.end_headers()
        reply_body = 'Saved "%s"\n' % filename
        self.wfile.write(reply_body.encode('utf-8'))

# Create a TCP/IP socket server
with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"Server listening on port {PORT}")
    httpd.serve_forever()
