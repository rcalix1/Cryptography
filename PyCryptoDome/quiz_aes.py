
from Crypto.Cipher import AES


# (key, mode, iv)

aes_code = AES.new('??????????', AES.MODE_ECB, 'abcdefgh')

#####################################################################

f_read_cipher = open('cipher.txt','r')
my_cipher = f_read_cipher.read()
f_read_cipher.close()

print aes_code.decrypt(my_cipher)
