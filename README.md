# Cryptography

Examples and code on cryptographic systems

## What is a secure cipher? 

XOR message with key as big as message (One Time Pad). Defined by Claude Shannon.

## OpenSSL

* openssl lets you generate RSA keys as short as 31 bits
* $ openssl genrsa 31
* $ openssl s_client -connect www.google.com:443
* ECC can be faster than RSA because it uses smaller numbers
* $ openssl speed ecdsap256 rsa4096

## TLS

* The protocol of SSL
* TLS stands for Transport Layer Security
* Current TLS version is around TLS 1.3
* TLS protocol handles the hand shake and the packet formatting for secure encapsulation of data
* The handshake relies on certificates and certificate authorities
* $ openssl s_client -connect www.google.com:443

## Is there any particular reason to use Diffie-Hellman over RSA for key exchange in TLS 1.3?

* ANSWER: Forward Secrecy
* TLS 1.3 uses an elliptic curve based Diffie Hellman approach
* Diffie-Hellman defines a key exchange mechanism that allows a client and a server to exchange secret keys in the presence of an eavesdropper
* In a TLS connection using the Diffie-Hellman key exchange, for every new connection from a client, the server typically generates a fresh Diffie-Hellman public-private key pair that is used to exchange keys for that session
* These are known as ephemeral key pairs
* The server’s long-term private key is only used to authenticate the server’s Diffie-Hellman public key (the ephemeral public key)
* Thus, if an attacker compromises the server’s long-term private key, they can impersonate the server but not be able to decrypt any previously encrypted communication
* SINCE The server’s private key was never used as part of the key-exchange (other than simply signing the ephemeral public keys)
* The Diffie-Hellman private keys that were used to compute the session keys are ephemeral
* i.e short lived for the duration of the handshake with that client and then discarded
* NOTE: Ephemeral Diffie-Hellman ciphers take the form TLS_DHE_ / TLS_ECDHE_ unlike their static Diffie-Hellman counterparts that take the form TLS_DH_/TLS_ECDH_
* In contrast, if you consider the RSA handshake in TLS, the client encrypts a random symmetric key to the server’s public key and the server uses it’s private key to decrypt and recover the symmetric key.
* This allows an attacker to passively observe and store encrypted network traffic (which used RSA key exchange for TLS communication)
* If the server’s private key is compromised, then the attacker can retrospectively decrypt the stored encrypted communication
* (since the session keys were encrypted to the server’s public key)
* The RSA key exchange is quite straightforward; the client generates a secret (a 46byte random number), encrypts it with the server’s public key, and sends it in the ClientKeyExchange message.
* To obtain the  secret, the server only needs to decrypt the message.
* The simplicity of the RSA key exchange is also its principal weakness.
* The  secret is encrypted with the server’s public key, which usually remains in use for several years.
* Anyone with access to the corresponding private key can recover the secret and construct the same secret, compromising session security.
* On Diffie-Hellman (DH) key exchange is a key agreement protocol that allows two parties to establish a shared secret over an insecure communication channel.
* The DH key exchange requires six parameters; two (dh_p and dh_g) are called domain parameters and are selected by the server.
* During the negotiation, the client and server each generate two additional parameters.
* Each side sends one of its parameters (dh_Ys and dh_Yc) to the other end, and, with some calculation, they arrive at the shared key.
* Diffie-Hellman (DH) key exchange is better than RSA because the two parties generate the new key together 
