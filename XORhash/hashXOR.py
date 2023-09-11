
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

def CreateBlocks(plain, block_size):
    temp_list_blocks = []
    for i in range(0, len(plain), block_size ):
        block = plain[i:i+block_size]
        if len(block) == block_size:
            temp_list_blocks.append( block  )
        else:
            c = block_size - len(block)
            for i in range(c):
                block = block + " "
            temp_list_blocks.append( block  )
    return temp_list_blocks

##################################################

def Hash_Func(list_of_blocks):
    cipher_block = "00001111"
    for block in list_of_blocks:
        print(block)
        ciper_block = block XOR cipher_block

##################################################
## Main()

plain_text = "this is a top secret 1234567890 AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ"
print( plain_text  )

length = 8

print( len( plain_text  )  )

list_of_blocks = CreateBlocks( plain_text, length  )

key = genkey(length)
print(key)

print(list_of_blocks)

hash_value = Hash_Func(list_of_blocks)



## cipher = Encrypt(plain_text, key)
## print( cipher  )

## plain_decrypted = Decrypt(cipher, key)
## print(plain_decrypted)

## print( "".join(plain_decrypted) )


##################################################
