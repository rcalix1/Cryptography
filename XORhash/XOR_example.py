

from os import urandom


##################################################

def genkey(length):
    ## generating the key
    return bytearray(  urandom(length)   )


#################################################

def Encrypt(plain, key):
    return bytearray( [ ord(plain[i]) ^  key[i]  for i in range(len(plain))   ]  )


##################################################

def Decrypt(cipher, key):
    return [ chr(  cipher[i] ^ key[i] )   for i in range(  len(cipher)  )     ]

##################################################
## Main()

plain_text = "this is a top secret"
print( plain_text  )

length = len(plain_text)

key = genkey(length)

## key_str = byte(  key   )

print(key)
## print(key_str)

cipher = Encrypt(plain_text, key)
print( cipher  )

plain_decrypted = Decrypt(cipher, key)
print(plain_decrypted)

print( "".join(plain_decrypted) )


##################################################
