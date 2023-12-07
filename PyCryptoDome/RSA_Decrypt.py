
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
#from Crypto.Cipher import AES


file_in = open("encrypted_data.bin", "rb")

enc_data = file_in.read()

f = open("private.pem")
key_in = f.read()
private_key = RSA.import_key(key_in)

cipher_RSA = PKCS1_OAEP.new(private_key)

plain_data = cipher_RSA.decrypt( enc_data  )

print(   plain_data   )
