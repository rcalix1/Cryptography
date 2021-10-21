## sign something 

from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

f = open('your_key.txt','r')
my_key = f.read()
key = RSA.import_key(my_key)
f.close()

message = b'To be signed'
hash = SHA256.new(message)

signature = pkcs1_15.new(key).sign(  hash   )


## receiver

f = open('another_key', 'r')

another_key = RSA.import_key(   f.read()    )
h = SHA256.new(message)
try:
    pkcs1_15.new(key).verify(h, signature)
    print("true")
except:
    print("false")
