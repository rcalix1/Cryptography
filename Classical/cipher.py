#Encrypt and decrypt using inverted numbers

import pprint

##################################

#  text = text.lower()
#  text.isdigit() != True

for i in range(len(text)):
    a = text[i]
    n1 = ord(a)
    code = convert(n1) ## a = 26, b = 25, and so on

   
    26 => 26
     3 => 03
    letter = chr(code)

####################################

def Encrypt(text):
    print text
    return cipher

def Decrypt(cipher):
    print cipher
    return cipher

##################################
## Main()

s = 'This is ITS 350 at Purdue University Northwest'
s_cipher = '07191889...242625'

result = Encrypt(s)
result2 = Decrypt(result)

##################################

print "<<<<<<<<DONE>>>>>>>>>"
