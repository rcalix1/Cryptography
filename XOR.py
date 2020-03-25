## xor script

from os import urandom
##########################################

def genKey(length):
    return bytearray(urandom(length))

##########################################
    
def encrypt1(plaintext, key):
    #print plaintext[i]
    return bytearray([ord(plaintext[i]) ^ key[i] for i in range(len(plaintext))])

#########################################

def encrypt2(plaintext, key):
    return bytearray([plaintext[i] ^ key[i] for i in range(len(plaintext))])
                  

##########################################


#########################################

def decrypt(ciphertext, key):
    return bytearray([ciphertext[i]  ^ key[i] for i in range(len(ciphertext)) ]  )

############################################

def decrypt2(ciphertext, key):
    ciphertext = str(ciphertext)
    return bytearray(  [ chr(ciphertext[i] ^ key[i])  for i in range(len(ciphertext))  ]   )

##########################################

def breakMessage(message):
    list_of_blocks = []
    for i in range(0, len(message),6):
        block = message[i:i+6]
        if (len(block) == 6):    
            list_of_blocks.append(block)
        else:
            c = 6 - len(block)
            for i in range(c):
                block = block + " "
            list_of_blocks.append(block)
    return list_of_blocks

##########################################

def main():
    myMessage = "this is the plain text"
    #key = genKey()

    blockList = breakMessage(myMessage)

    print blockList

    key =  genkey(  len(blockList[0])  )

    print str(key)

    initialization_vector = genkey(   len(blockList[0])   )

    list_of_ciphers = []

    for i in range(len(blockList)):
        initialize_cipher = encrypt1(blockList[i],initialization_vector)
        cipherBlock = encrypt2(initialize_cipher, key)
        list_of_cipers.append(cipherBlock)
        initialize_cipher = cipherBlock

    print list_of_ciphers
    list_decrypted_blocks = []
    for i in range(   len(list_of_ciphers)   ):
        initialize_cipher = decrypt(list_of_ciphers[i], key)
        if i > 0: 
            decrypted_block = decrypt(initialize_cipher, list_of_ciphers[i-1])
        else:
            decrypted_block = decrypt(initialize_cipher, initialization_vector)
        list_decypted_blocks.append(decrypted_block

)
    #cipher = encrypt(myMessage, key)
    #print str(cipher)
    #decrypted_message = decrypt(cipher, key)
    #print decrypted_message

    #if decrypt(encrypt(myMessage,key), key) == myMessage:
    #    print "it works" 
    #else:
    #    print "something failed"

#########################################

main()



##########################################

print "<<<<<<<<<<<<<DONE>>>>>>>>>>>>>>"
