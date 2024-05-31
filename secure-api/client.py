import ssl
import urllib.request

# Client configuration
url = 'https://localhost:8443'

# Create an SSL context
context = ssl.create_default_context()
context.load_verify_locations('server.crt')
context.load_cert_chain(certfile='client.crt', keyfile='client.key')

# Make an HTTPS request
req = urllib.request.Request(url)
with urllib.request.urlopen(req, context=context) as response:
    print(response.read().decode())

