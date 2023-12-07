from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import MD5

######################################

def create_keys():
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)
    public_key = key.publickey()
    string_private_key = key.exportKey()
    string_public_key = public_key.exportKey()
    print string_private_key
    print string_public_key
    write_pub = open("public_key.txt",'w')
    write_pub.write(string_public_key)
    write_pub.close()
    write_private = open("private_key.txt", 'w')
    write_private.write(string_private_key)
    write_private.close()

######################################

def encrypt():
    read_plain = open("input_message.txt", 'r')
    message = read_plain.read()
    read_plain.close()
    read_key = open("public_key.txt", 'r')
    temp_string = read_key.read()
    read_key.close()
    key = RSA.importKey(temp_string)
    cipher =  key.encrypt(message, 32)
    print cipher
    write_cipher = open("cipher.txt", 'w')
    write_cipher.write(cipher[0])
    write_cipher.close()

#####################################

def decrypt():
    key_file = open("private_key.txt",'r')
    key_string = key_file.read()
    key_file.close()
    cipher_file = open("cipher.txt",'r')
    cipher_text = cipher_file.read()
    cipher_file.close()
    key = RSA.importKey(key_string)
    plain = key.decrypt(cipher_text)
    print plain 

#####################################

def sign():
    random_number = Random.new().read
    key_file = open('private_key.txt','r')
    temp_string = key_file.read()
    key_file.close()
    data_file = open("cipher.txt",'r')
    message = data_file.read()
    data_file.close()
    key = RSA.importKey(temp_string)
    m = MD5.new()
    m.update(message)
    hash = m.digest() 
    signature = key.sign(hash, random_number)
    print signature
    file_signature = open("signature.txt",'w')
    file_signature.write(  str(signature[0])  )
    file_signature.close()


#####################################

def verify():
    key_file = open("public_key.txt", 'r')
    temp_string = key_file.read()
    key_file.close()
    signature_file = open("signature.txt", 'r')
    signature_string = signature_file.read()
    signature_file.close()
    cipher_file = open("cipher.txt",'r')
    cipher_message = cipher_file.read()
    cipher_file.close()
    m = MD5.new()
    m.update(cipher_message)
    hash = m.digest()
    signature = (long(signature_string),)
    key = RSA.importKey(temp_string)
    print key.verify(hash, signature)

######################################
## MAIN()

create_keys()
encrypt()
decrypt()
sign()
verify()

######################################
