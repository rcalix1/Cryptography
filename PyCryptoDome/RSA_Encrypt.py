
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

data = b"this is fall 2021"

#data2= "this is another text example".encode("utf-8")

file_out = open("encrypted_data.bin", "wb")

f = open("public.pem")
key_in = f.read()
public_key = RSA.import_key(key_in)


cipher_RSA = PKCS1_OAEP.new(public_key)

enc_data = cipher_RSA.encrypt( data  )

file_out.write(  enc_data    ) 
file_out.close()
