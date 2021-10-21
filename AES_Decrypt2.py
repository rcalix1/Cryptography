
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

file_in =  open("AES_encrypted.bin", "rb")

iv = file_in.read(16)

cipher_text = file_in.read()
file_in.close()

file_key = open("AES_key.txt", "rb")

## read also the secret key
secret_key = file_key.read()
file_key.close()
## read also the tag

cipher_AES = AES.new(secret_key, AES.MODE_CBC, iv=iv)
decrypted_message = cipher_AES.decrypt(cipher_text)


print(decrypted_message)
