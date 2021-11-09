from Crypto.PublicKey import RSA
from Crypto import Random

def decrypt():
     f_key = open('???????','r')
     string_key = f_key.read()
     f_key.close()
     key2 = RSA.importKey(string_key)
     f_symmetric_key = open('symmetric_cipher.txt','r')
     symmetric_key_cipher = f_symmetric_key.read()
     f_symmetric_key.close()
     print key2.decrypt(symmetric_key_cipher)
     


#create_keys()
encrypt()
decrypt()
