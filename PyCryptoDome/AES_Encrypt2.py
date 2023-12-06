
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b"rc34567891234567"

secret_key = get_random_bytes(16)

file_key = open("AES_key.txt", "wb")
file_key.write(secret_key)
file_key.close()

cipher_AES = AES.new(secret_key, AES.MODE_CBC)
cipher_text = cipher_AES.encrypt(data)


file_out = open("AES_encrypted.bin", "wb")
file_out.write(cipher_AES.iv)
file_out.write(cipher_text)
file_out.close()
