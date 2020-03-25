from Crypto.Cipher import DES

obj = DES.new('abcdefgh', DES.MODE_ECB)

plain = 'today is tuesdat october 15, 2019'

print len(plain)

cipher = obj.encrypt(plain + 'xxxxxxx')

print cipher

print obj.decrypt(cipher)

#################################

obj_alice = DES.new('abcdefgh',DES.MODE_ECB)
print obj_alice.decrypt(cipher)
