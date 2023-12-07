
from os import urandom
import pickle

#######################################

def genKey(length):
    return bytearray(  urandom(length)   )

#####################################

def decrypt1(cipher, key):
    return bytearray( cipher[i] ^ key[i] for i in range(len(cipher))   )

######################################

def decrypt2(cipher, key):
    return [ chr( cipher[i] ^ key[i]) for i in range( len(cipher)  )]


######################################

def encrypt1(plain_block, key):
    return bytearray( [  ord( plain_block[i])  ^ key[i] for i in range( len(plain_block)   )  ] )

#######################################


def encrypt2(plain_block, key):
    return bytearray(  [  plain_block[i] ^ key[i]   for i in range( len(plain_block)    )]        )


#######################################

def encrypt_message(blockList, key, iv, len_of_block):
    list_of_ciphers = []
    for i in range(  len(blockList)    ):
        cipher1 = encrypt1(blockList[i], iv)
        cipher2 = encrypt2(cipher1, key)
        list_of_ciphers.append( cipher2  )
        iv = cipher2
    return list_of_ciphers


#######################################

def decrypt_cipher(list_cipher, key, iv):
    list_of_decrypted_blocks = []
    for i in range( len(list_cipher)   ):
        if i == 0:
            temp  = decrypt1( list_cipher[i], key)
            plain = decrypt2(temp, iv)
        else:
            temp  = decrypt1(list_cipher[i], key)
            plain = decrypt2(temp, list_cipher[i-1]) 
        list_of_decrypted_blocks.append(  plain   )
    return list_of_decrypted_blocks


########################################

def breakMessage(message, len_of_block):
    list_of_blocks = []
    for i in range(0, len(message), len_of_block):
        block = message[i:i+len_of_block]
        if ( len(block) == len_of_block ):
            list_of_blocks.append( block  )
        else:
            c = len_of_block - len(block)
            for i in range(c):
                block = block + " "
            list_of_blocks.append(block)
    return list_of_blocks



########################################

def main():

    myMessage = "this is a message 1234567890987654321qwretrutiyp gdgfsvxv jdhfyti jfh"

    ## print("enter a message to encrypt: ")
    ## myMessage = input()

    f_in = open("plain_text_cbc.txt", 'r')

    myMessage = f_in.read()
    myMessage = myMessage.replace("\n", "")
    print(myMessage)

    len_of_block = 8

    blockList = breakMessage(myMessage, len_of_block)

    print( blockList  )

    key = genKey(len_of_block)
    
    iv  = genKey(len_of_block)

    print( key  )

    print( iv   )


    cipher_list = encrypt_message(blockList, key, iv, len_of_block)

    print(  cipher_list   )
    
    f_out = open("the_cipher.bin", "w")

    for i in range(len(cipher_list)):
        str_cipher = str(  cipher_list[i]   )
        print(str_cipher)
        print(cipher_list[i])
        f_out.write(str_cipher + "\n" )
    f_out.close()

    ###############################################

    file_x = open('pickle_cipher_list', 'wb')
    pickle.dump(cipher_list, file_x)
    file_x.close()

    ###############################################

    file_y = open('pickle_cipher_list', 'rb')
    from_pickle_cipher_list = pickle.load(file_y)
    file_y.close()

    ###############################################
    print('******************************')
    print('after pickle')
    pk_decrypted_list = decrypt_cipher(  from_pickle_cipher_list, key, iv   )

    print(pk_decrypted_list)


    return




########################################


main()
