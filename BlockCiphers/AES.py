from os import urandom
import pickle

#######################################

def genKey(length):
    return bytearray(urandom(length))

#######################################

# 4-bit AES-like SBOX
SBOX = bytes([0x6, 0x4, 0xC, 0x5, 0x0, 0x7, 0x2, 0xE,
              0x1, 0xF, 0x3, 0xD, 0x8, 0xA, 0x9, 0xB])
INV_SBOX = [SBOX.index(i) for i in range(16)]

def sub_bytes(block):
    return bytearray([SBOX[b & 0x0F] for b in block])

def inv_sub_bytes(block):
    return bytearray([INV_SBOX[b & 0x0F] for b in block])

def shift_rows(block):
    return bytearray([
        block[0], block[5], block[2], block[7],
        block[4], block[1], block[6], block[3]
    ])

def inv_shift_rows(block):
    return bytearray([
        block[0], block[5], block[2], block[7],
        block[4], block[1], block[6], block[3]
    ])

#######################################

def encrypt1(plain_block, key):
    # Convert str to bytes and XOR with IV (AddRoundKey pre-CBC)
    state = bytearray([ord(plain_block[i]) ^ key[i] for i in range(len(plain_block))])
    state = sub_bytes(state)
    state = shift_rows(state)
    return state

def decrypt1(cipher, key):
    state = inv_shift_rows(cipher)
    state = inv_sub_bytes(state)
    return bytearray([state[i] ^ key[i] for i in range(len(state))])

#######################################

def decrypt2(cipher, key):
    return [chr(cipher[i] ^ key[i]) for i in range(len(cipher))]

#######################################

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
