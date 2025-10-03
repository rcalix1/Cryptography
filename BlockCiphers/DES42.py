from os import urandom

import pickle


#############################
## generating the key

def genkey( length ):
    return bytearray( urandom( length ) )


#############################

def Encrypt( plain, key ):
    
    return  bytearray(  [   ord( plain[i] ) ^ key[i]    for i in range(  len(plain)   )   ]  ) 


#############################

##                 4    4   8
def feistel_round( R0,   L0, iv):

    F_out = encrypt2( R0 , iv[:4] )
    ### L = L0 ^ F_out
    R1 = encrypt2( L0, F_out )
    
    L1 = R0
    

    return  R1 , L1

############################


def feistel_round_reverse( R1,   L1, iv):
    
    F_out = encrypt2( L1 , iv[:4] )
    ### L = L0 ^ F_out

    L0 = encrypt2( R1, F_out ) 
       
    R0 = L1

    return  R0 , L0


#############################


def encrypt1( plain_block  ,  iv  ):

    temp_block = Encrypt( plain_block, iv   )

    ## print( temp_block )
    ##############################
    ## DES

    R = temp_block[ : 4 ]
    L = temp_block[4:   ]

    for _ in range(3):     ## 3 feistel rounds
  
        R, L = feistel_round( R, L,  iv   )
        
    ##############################
    return R + L



##################################

def decrypt2( temp, key   ):

    R1, L1 = temp[ : 4], temp[4:]

    for _ in range(3):  ## 3 feistel rounds in reverse
        
        ## L1 = L0 ^ iv ^ R0
 
        R0, L0  = feistel_round_reverse(  R1, L1, key    )
       
    concat_halves = R0 + L0

    res = decrypt_to_plain_letter(  concat_halves , key   )

    return res
    

##################################

def encrypt2( temp_cipher_block, key  ):
    print( temp_cipher_block   ) 
    print( key  )
    return bytearray(   [   temp_cipher_block[i] ^ key[ i ]     for i in range(  len(temp_cipher_block)   )]     )

#################################

def decrypt_to_plain_letter(  cipher_block, iv   ):

    return [  chr( cipher_block[i] ^ iv[i] )   for i in range(  len(cipher_block)   )    ]     


#################################


def decrypt1( temp_cipher, iv  ):

    return bytearray(      [    temp_cipher[i] ^ iv[i]      for i in range(      len(temp_cipher)       )      ]              )



#################################


def Decrypt(   cipher,  key  ):

    return [      chr(  cipher[i] ^ key[i] )      for i in range(   len(cipher)     )  ]

###############################


def encrypt_message(   blockList, key, iv, len_of_blocks    ):

    list_of_ciphers = []

    for i in range(    len(blockList)     ):
        cipher1 = encrypt1( blockList[i]  ,  key     )

        cipher2 = encrypt2( cipher1       , iv  )

        list_of_ciphers.append(  cipher2   )
        iv = cipher2
    return list_of_ciphers



###############################

def decrypt_cipher( list_cipher, key, iv  ):

    list_of_decrypted_blocks = []
    for i in range(   len(list_cipher)    ):
        index = len( list_cipher ) - i - 1
        if i == 0:
            iv = iv
        else:
            iv = list_cipher[ index - 1 ]

        temp  = decrypt1(  list_cipher[ index ] , iv  )
      
        plain = decrypt2(  temp, key   )
       

        list_of_decrypted_blocks.append(  plain    )

    return list_of_decrypted_blocks



        
        





###############################


def CreateBlocks( plain, block_size ):

    temp_list_blocks = []
    for i in range(0, len(plain), block_size  ):
        block = plain[i:i+block_size]
        if len( block  ) == block_size:
            temp_list_blocks.append(  block   )
        else:
            c = block_size - len(  block   )
            for i in range( c  ):
                block = block + " "
            temp_list_blocks.append(  block    )
    return temp_list_blocks




###############################
## Main()



plain_text = "this is a top secret 1234567890 AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ"

print( plain_text  )

length = 8

print( len(plain_text)  )

#################################



list_of_blocks = CreateBlocks( plain_text, length    )


print(  list_of_blocks   )


#################################

key = genkey(  length  )
iv  = genkey(  length  )


print(  key  )
print(  iv   )

################################

cipher_list = encrypt_message(  list_of_blocks, key, iv, length     )

print(   cipher_list    )

################################
## Decrypt 


after_pickle_decrypted_plain = decrypt_cipher(  cipher_list, key, iv    )

print( after_pickle_decrypted_plain  )


## print(  ''.join(  [  ''.join(  block   )   for block in after_pickle_decrypted_plain ]   )   )






print("DONE")
