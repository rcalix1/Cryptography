from Crypto.Hash import MD5
from Crypto.PublicKey import RSA
from Crypto import Random

rng = Random.new().read

RSAkey = RSA.generate(1024, rng)

plaintext = 'ubuntu linux machine'

hash = MD5.new(plaintext).digest()

signature = RSAkey.sign(hash, rng)
print signature

print RSAkey.verify(hash, signature)
print RSAkey.verify(hash[:-1], signature)
