import ssl
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, this is a secure server!")

def run(server_class=HTTPServer, handler_class=SimpleHandler):
    server_address = ('', 8443)
    httpd = server_class(server_address, handler_class)
    
    # Load the server certificate and private key
    httpd.socket = ssl.wrap_socket(httpd.socket,
                                   server_side=True,
                                   certfile='server.crt',
                                   keyfile='server.key',
                                   ssl_version=ssl.PROTOCOL_TLS)
    
    print('Starting https server on port 8443...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
