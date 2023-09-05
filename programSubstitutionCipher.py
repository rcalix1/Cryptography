
import pprint

#############################################################

def func_cipher(ascii_val):
    ## a -> 26
    ## b -> 25
    cipher_code = 27 - (ascii_val - 96)
    return cipher_code

#############################################################

def func_plain(code_val):
    ## 26 -> a
    ## 25 -> b
    plain_code = 96 + (27 - code_val)
    return plain_code

#############################################################

def Encrypt(plain):
    scode = ""
    text = plain.lower()
    plain_length = len(plain)
    for i in range(   plain_length    ):
        letter = plain[i]
        ascii_val = ord(letter )
        code = func_cipher(ascii_val)
        if code < 10:
            scode = scode + '0' + str( code  )
        else:
            scode = scode + str( code )
        ## print(ascii_val)
    ## print(plain_length)
    return scode


#############################################################

def Decrypt(cipher):
    plain_decrypted = ""
    length_cipher = len(cipher)
    ##print(length_cipher)
    for i in range(0, length_cipher, 2):
        ##print(i)
        ##print(cipher[i] + cipher[i+1])
        the_code = int(    cipher[i] + cipher[i+1]       )
        ascii_val = func_plain( the_code  )
        letter = chr(ascii_val)
        plain_decrypted = plain_decrypted + letter
    return plain_decrypted


#############################################################
## main()

## Do this for 26 letters
## a -> 26
## b -> 25
## c -> 24

## plain_text = "today is Tuesday and my name john smith"
## cipher     = "this will the cipher"


print("Please enter your message to encrypt:")
plain_text = input()

cipher           = Encrypt(plain_text)

print(cipher)
decrypted_cipher = Decrypt(cipher)

print(decrypted_cipher)




#############################################################
