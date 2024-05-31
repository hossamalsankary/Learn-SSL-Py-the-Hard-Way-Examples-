# CA 
openssl genrsa -out rootCA.key 2048
openssl req -x509 -new -nodes -key rootCA.key -sha256 -days 1024 -out rootCA.crt -subj "/C=US/ST=California/L=San Francisco/O=My Company/OU=My Department/CN=MyRootCA"

#Server Certificate
openssl genrsa -out server.key 2048
openssl req -new -key server.key -out server.csr -subj "/C=US/ST=California/L=San Francisco/O=My Company/OU=My Department/CN=localhost"
openssl x509 -req -in server.csr -CA rootCA.crt -CAkey rootCA.key -CAcreateserial -out server.crt -days 500 -sha256 -extfile <(echo "subjectAltName=DNS:localhost")


#Client Certificate:

openssl genrsa -out client.key 2048
openssl req -new -key client.key -out client.csr -subj "/C=US/ST=California/L=San Francisco/O=My Company/OU=My Department/CN=client"
openssl x509 -req -in client.csr -CA rootCA.crt -CAkey rootCA.key -CAcreateserial -out client.crt -days 500 -sha256 -extfile <(echo "subjectAltName=DNS:client")



