
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b"today is thursday october 21, 2021"

secret_key = get_random_bytes(16)

cipher_AES = AES.new(secret_key, AES.MODE_EAX)
cipher_text, tag = cipher_AES.encrypt_and_digest(data)


file_out = open("AES_encrypted.bin", "wb")
file_out.write(cipher_text)
file_out.close()
