# Learn SSL_Py the Hard Way Examples

## Introduction

Welcome to **Learn SSL_Py the Hard Way Examples**! This repository is a comprehensive guide for setting up secure communication between a Python server and client using SSL/TLS certificates. Through detailed examples, we'll cover the generation of certificates, configuration of both server and client, and verification using `curl`. This hands-on approach will ensure you understand each step involved in securing Python applications.

## Prerequisites

Make sure you have the following tools installed on your system:
- Python 3.x
- OpenSSL
- `curl`

## Step-by-Step Guide

### 1. Generating SSL Certificates

We'll start by generating the SSL certificates needed for the server and client using OpenSSL.

#### Create a Configuration File

First, create a configuration file named `openssl.cnf` with the following content:

```cnf
[req]
distinguished_name = req_distinguished_name
x509_extensions = v3_req
prompt = no

[req_distinguished_name]
C = US
ST = California
L = San Francisco
O = My Company
OU = My Department
CN = localhost

[v3_req]
keyUsage = keyEncipherment, dataEncipherment
extendedKeyUsage = serverAuth
subjectAltName = @alt_names

[alt_names]
DNS.1 = localhost

