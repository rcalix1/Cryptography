# ITS 350
# Lab RSA - Student Problem

import pickle

from random import randrange, getrandbits
from itertools import repeat
from functools import reduce
from math import log10
from time import time

#####################################################################
 
def getPrime(n):
    """Get a n-bit pseudo-random prime"""
    def isProbablePrime(n, t = 7):
        """Miller-Rabin primality test"""
        def isComposite(a):
            """Check if n is composite"""
            if pow(a, d, n) == 1:
                return False
            for i in range(s):
                if pow(a, 2 ** i * d, n) == n - 1:
                    return False
            return True
     
        assert n > 0
        if n < 3:
            return [False, False, True][n]
        elif not n & 1:
            return False
        else:
            s, d = 0, n - 1
            while not d & 1:
                s += 1
                d >>= 1
        for _ in repeat(None, t):
            if isComposite(randrange(2, n)):
                return False
        return True   
     
    p = getrandbits(n)
    while not isProbablePrime(p):
        p = getrandbits(n)
    return p

########################################################
## to get the d exponent

## d*e mod phi = 1

##      e, phi
def inv(p, q):
    """Multiplicative inverse"""
    def xgcd(x, y):
        """Extended Euclidean Algorithm"""
        s1, s0 = 0, 1
        t1, t0 = 1, 0
        while y:
            q = x // y
            x, y = y, x % y
            s1, s0 = s0 - q * s1, s1
            t1, t0 = t0 - q * t1, t1
        return x, s0, t0      
 
    s, t = xgcd(p, q)[0:2]
    assert s == 1
    if t < 0:
        t += q
    return t

######################################################################

def genRSA(p, q):
    """Generate public and private keys"""
    #  This section to be completed by student

    n = p * q
    phi = (p-1)*(q-1)

    if n < 65537:
        e = 3
        d = inv(e, phi)
    else:
        e = 65537
        d = inv(e, phi)
    return (e, d, n)

#######################################################################
## Various utility functions
#######################################################################

def text2Int(text):
    """Convert a text string into an integer"""
    return reduce(lambda x, y : (x << 8) + y, map(ord, text))
 
def int2Text(number, size):
    """Convert an integer into a text string"""
    text = "".join([chr((number >> j) & 0xff)
                    for j in reversed(range(0, size << 3, 8))])
    return text.lstrip("\x00")
 
def int2List(number, size):
    """Convert an integer into a list of small integers"""
    return [(number >> j) & 0xff
            for j in reversed(range(0, size << 3, 8))]
 
def list2Int(listInt):
    """Convert a list of small integers into an integer"""
    return reduce(lambda x, y : (x << 8) + y, listInt)
 
def modSize(mod):
    """Return length (in bytes) of modulus"""
    modSize = len("{0:02x}".format(mod)) // 2
    return modSize

########################################################################
 
def encrypt(ptext, pk, mod):
    """Encrypt message with public key"""
    size = modSize(mod)
    output = []
    while ptext:
        nbytes = min(len(ptext), size - 1)
        aux1 = text2Int(ptext[:nbytes])
        assert aux1 < mod
        aux2 = pow(aux1, pk, mod)
        output += int2List(aux2, size + 2)
        ptext = ptext[size:]
    return output

######################################################################

def decrypt(ctext, sk, p, q):
    """Decrypt message with private key
    using the Chinese Remainder Theorem"""
    mod = p * q
    size = modSize(mod)
    output = ""
    while ctext:
        aux3 = list2Int(ctext[:size + 2])
        assert aux3 < mod
        m1 = pow(aux3, sk % (p - 1), p)
        m2 = pow(aux3, sk % (q - 1), q)
        h = (inv(q, p) * (m1 - m2)) % p
        aux4 = m2 + h * q
        output += int2Text(aux4, size)
        ctext = ctext[size + 2:]
    return output


####################################################################

def printHexList(intList):
        """Print ciphertext in hex"""
        for index, elem in enumerate(intList):
            if index % 32 == 0:
                print(),            
            print("{0:02x}".format(elem)),
        print()


###################################################################
###################################################################
##Main Start
###################################################################
## To be completed by student
## This section to be completed by student

seed_size = 256   ## 256, 512, 1024, 2048, 4096

p = getPrime(seed_size)
q = getPrime(seed_size)

print(p)
print(q)


## plain_message = "Claude Shannon is the father of cryptography"   ## this is where the  AES-CBC key would go
plain_message = "13245636782345784asd"


e, d, n = genRSA(p, q)


public_key  = (e, n)
private_key = (d, n)

print(n)
print(e)
print(d)

print(public_key)
print(private_key)

cipher = encrypt(plain_message, e, n)

############################################

file_x = open('pickle_cipher', 'wb')
pickle.dump(cipher, file_x)
file_x.close()

############################################

file_y = open('pickle_cipher', 'rb')
from_pickle_cipher = pickle.load(file_y)
file_y.close()

############################################

print(cipher)
printHexList(cipher)

## write to file using pickle

decrypted_plain = decrypt(from_pickle_cipher, d, p, q)
print( decrypted_plain  )

print('<<<<<<<<<<<<<DONE>>>>>>>>>>>>')
## End
#################################################################


