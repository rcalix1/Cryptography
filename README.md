# Cryptography

Examples and code on cryptographic systems

## What is a secure cipher? 

XOR message with key as big as message (One Time Pad). Defined by Claude Shannon.

## OpenSSL

* openssl lets you generate RSA keys as short as 31 bits
* $ openssl genrsa 31

## TLS

* The protocol of SSL
* TLS stands for Transport Layer Security
* Current TLS version is around TLS 1.3
* TLS protocol handles the hand shake and the packet formatting for secure encapsulation of data
* The handshake relies on certificates and certificate authorities
* $ openssl s_client -connect www.google.com:443
* 
