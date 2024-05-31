import ssl
import urllib.request

# Client configuration
url = 'https://localhost:8443'

# Create an SSL context with strict verification
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_verify_locations('./ssl/rootCA.crt')
context.load_cert_chain(certfile='./ssl/client.crt', keyfile='./ssl/client.key')

# Make an HTTPS request
req = urllib.request.Request(url)
with urllib.request.urlopen(req, context=context) as response:
    print(response.read().decode())
