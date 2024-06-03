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
    
    # Create SSL context
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    
    # Load the server certificate and private key
    context.load_cert_chain(certfile='./ssl/server.crt', keyfile='./ssl/server.key')
    
    # Set client certificate requirements and CA certificate file
    context.verify_mode = ssl.CERT_REQUIRED
    context.load_verify_locations(cafile='./ssl/rootCA.crt')
    
    # Wrap the server socket with SSL
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    
    print('Starting https server on port 8443...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()    