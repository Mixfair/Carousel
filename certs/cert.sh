#!/bin/bash

#
# openssl req \
# 	-x509 \
# 	-newkey rsa:4096 \
# 	-keyout cakey.pem \
# 	-out cacert.pem \
# 	-nodes \
# 	-days 365 \
#   -config req.cnf \
#   -extensions v3_ca
#
# openssl req \
#   -newkey rsa:4096 \
#   -keyout intermediate-key.pem \
#   -out intermediate-csr.pem \
#   -nodes \
#   -config req_inter.cnf \
#   -days 365
#
# openssl x509 \
# 	-req \
# 	-in intermediate-csr.pem \
# 	-CA cacert.pem \
# 	-CAkey cakey.pem \
#   -CAcreateserial \
#   -out intermediate-cert.pem \
#   -days 365 \
#   -extfile req_inter.cnf \
#   -extensions v3_ca

cat cacert.pem intermediate-cert.pem > ca-chain.pem

openssl req \
  -newkey rsa:4096 \
  -keyout server-key.pem \
  -out server-csr.pem \
  -nodes \
  -days 365 \

openssl x509 \
	-req \
	-in server-csr.pem \
	-CA intermediate-cert.pem \
	-CAkey intermediate-key.pem \
  -CAcreateserial \
  -out server-cert.pem \
  -days 365 \
  -extfile req_certs.cnf \
  -extensions server_cert

openssl req \
  -newkey rsa:4096 \
  -keyout client-key.pem \
  -out client-csr.pem \
  -nodes \
  -days 365 \

openssl x509 \
	-req \
	-in client-csr.pem \
	-CA intermediate-cert.pem \
	-CAkey intermediate-key.pem \
  -CAcreateserial \
  -out client-cert.pem \
  -days 365 \
  -extfile req_certs.cnf \
  -extensions usr_cert

# chmod 777 cert.pem cacert.pem key.pem
