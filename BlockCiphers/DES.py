from os import urandom
import pickle

#######################################

def genKey(length):
    return bytearray(urandom(length))

#######################################

def feistel_round(L, R, k):
    F_out = R ^ k
    return R, L ^ F_out

def encrypt1(plain_block, iv):
    block = bytearray([ord(plain_block[i]) ^ iv[i] for i in range(len(plain_block))])
    L, R = block[:4], block[4:]
    for _ in range(3):  # 3 rounds
        L0, R0 = L[0], R[0]
        R_new, L_new = feistel_round(L0, R0, iv[0])
        L, R = bytearray([L_new]), bytearray([R_new])
    return L + R

def decrypt1(cipher, key):
    L, R = cipher[:1], cipher[1:2]
    for _ in range(3):
        L_new = R[0] ^ (L[0] ^ key[0])
        L, R = bytearray([L_new]), L
    out = L + R
    return bytearray([out[i] ^ key[i] for i in range(len(out))])

######################################

def decrypt2(cipher, key):
    return [chr(cipher[i] ^ key[i]) for i in range(len(cipher))]

######################################

def encrypt2(plain_block, key):
    return bytearray([plain_block[i] ^ key[i] for i in range(len(plain_block))])

#######################################

def encrypt_message(blockList, key, iv, len_of_block):
    list_of_ciphers = []
    for i in range(len(blockList)):
        cipher1 = encrypt1(blockList[i], iv)
        cipher2 = encrypt2(cipher1, key)
        list_of_ciphers.append(cipher2)
        iv = cipher2
    return list_of_ciphers

#######################################

def decrypt_cipher(list_cipher, key, iv):
    list_of_decrypted_blocks = []
    for i in range(len(list_cipher)):
        if i == 0:
            temp = decrypt1(list_cipher[i], key)
            plain = decrypt2(temp, iv)
        else:
            temp = decrypt1(list_cipher[i], key)
            plain = decrypt2(temp, list_cipher[i - 1])
        list_of_decrypted_blocks.append(plain)
    return list_of_decrypted_blocks

########################################

def breakMessage(message, len_of_block):
    list_of_blocks = []
    for i in range(0, len(message), len_of_block):
        block = message[i:i + len_of_block]
        if len(block) < len_of_block:
            block += " " * (len_of_block - len(block))
        list_of_blocks.append(block)
    return list_of_blocks

########################################

def main():
    f_in = open("plain_text_cbc.txt", 'r')
    myMessage = f_in.read().replace("\n", "")
    f_in.close()
    print("Original message:", myMessage)

    len_of_block = 8
    blockList = breakMessage(myMessage, len_of_block)
    print("Blocks:", blockList)

    key = genKey(len_of_block)
    iv = genKey(len_of_block)

    print("Key:", key)
    print("IV: ", iv)

    cipher_list = encrypt_message(blockList, key, iv, len_of_block)
    print("Encrypted blocks:", cipher_list)

    with open("the_cipher.bin", "w") as f_out:
        for cipher in cipher_list:
            str_cipher = str(cipher)
            print(str_cipher)
            f_out.write(str_cipher + "\n")

    with open('pickle_cipher_list', 'wb') as file_x:
        pickle.dump(cipher_list, file_x)

    with open('pickle_cipher_list', 'rb') as file_y:
        from_pickle_cipher_list = pickle.load(file_y)

    print('******************************')
    print('After pickle load & decryption:')
    pk_decrypted_list = decrypt_cipher(from_pickle_cipher_list, key, iv)
    print(''.join([''.join(block) for block in pk_decrypted_list]))

########################################

main()
