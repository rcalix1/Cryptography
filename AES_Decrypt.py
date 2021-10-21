
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

file_in =  open("AES_encrypted.bin", "rb")
cipher_text = file_in.read()
file_in.close()

## read also the secret key

## read also the tag

cipher_AES = AES.new(secret_key, AES.MODE_EAX)
decrypted_message = cipher_AES.decrypt_and_verify(cipher_text, tag)


print(decrypted_message)
