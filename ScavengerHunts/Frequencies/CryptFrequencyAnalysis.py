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

    for letter in text:

        ## Keep only letters a-z

        if letter >= 'a' and letter <= 'z':

            ascii_val = ord(letter)

            code = func_cipher(ascii_val)

            if code < 10:
                scode = scode + '0' + str(code)
            else:
                scode = scode + str(code)

    return scode

#############################################################

def Decrypt(cipher):

    plain_decrypted = ""

    length_cipher = len(cipher)

    for i in range(0, length_cipher, 2):

        the_code = int(cipher[i] + cipher[i+1])

        ascii_val = func_plain(the_code)

        letter = chr(ascii_val)

        plain_decrypted = plain_decrypted + letter

    return plain_decrypted

#############################################################

def Frequency(cipher):

    frequencies = {}

    for i in range(0, len(cipher), 2):

        the_code = cipher[i:i+2]

        if the_code not in frequencies:
            frequencies[the_code] = 0

        frequencies[the_code] += 1

    return frequencies

#############################################################

def Probability(frequencies):

    probabilities = {}

    total = sum(frequencies.values())

    for code in frequencies:

        probabilities[code] = frequencies[code] / total

    return probabilities

#############################################################
## Find sequences of cipher symbols
##
## size = 2 --> bigrams
## size = 3 --> trigrams

def Sequence_Frequency(cipher, size):

    frequencies = {}

    symbols = []

    ## Break cipher into two-digit symbols

    for i in range(0, len(cipher), 2):

        symbols.append(cipher[i:i+2])

    ## Count sequences

    for i in range(len(symbols) - size + 1):

        sequence = ""

        for j in range(size):

            sequence = sequence + symbols[i+j]

        if sequence not in frequencies:
            frequencies[sequence] = 0

        frequencies[sequence] += 1

    return frequencies

#############################################################
## Typical English letter frequencies
## Percentages

english_frequency = {

    'a': 8.17,
    'b': 1.49,
    'c': 2.78,
    'd': 4.25,
    'e': 12.70,
    'f': 2.23,
    'g': 2.02,
    'h': 6.09,
    'i': 6.97,
    'j': 0.15,
    'k': 0.77,
    'l': 4.03,
    'm': 2.41,
    'n': 6.75,
    'o': 7.51,
    'p': 1.93,
    'q': 0.10,
    'r': 5.99,
    's': 6.33,
    't': 9.06,
    'u': 2.76,
    'v': 0.98,
    'w': 2.36,
    'x': 0.15,
    'y': 1.97,
    'z': 0.07
}

#############################################################
## Some common English bigrams

english_bigrams = [

    "th",
    "he",
    "in",
    "er",
    "an",
    "re",
    "on",
    "at",
    "en",
    "nd"

]

#############################################################
## Some common English trigrams

english_trigrams = [

    "the",
    "and",
    "ing",
    "her",
    "ere",
    "ent",
    "tha",
    "nth",
    "was",
    "eth"

]

#############################################################
## main()
##
## Read plaintext from file

filename = "HuckFinn.txt"

with open(filename, "r") as file:

    plain_text = file.read()

#############################################################

print("\nOriginal Text")
print("-------------")

print(plain_text)

#############################################################
## Encrypt

cipher = Encrypt(plain_text)

print("\nCipher")
print("------")

print(cipher)

#############################################################
## Decrypt

decrypted_cipher = Decrypt(cipher)

print("\nDecrypted")
print("---------")

print(decrypted_cipher)

#############################################################
## Single symbol frequency analysis

frequencies = Frequency(cipher)

probabilities = Probability(frequencies)

sorted_cipher = sorted(
    probabilities.items(),
    key=lambda x: x[1],
    reverse=True
)

sorted_english = sorted(
    english_frequency.items(),
    key=lambda x: x[1],
    reverse=True
)

#############################################################

print("\nCipher Frequency Analysis")
print("-------------------------")

for code, probability in sorted_cipher:

    print(
        code,
        " -> ",
        round(probability * 100, 2),
        "%"
    )

#############################################################

print("\nEnglish Letter Frequencies")
print("--------------------------")

for letter, probability in sorted_english:

    print(
        letter,
        " -> ",
        probability,
        "%"
    )

#############################################################
## Compare rankings

print("\nPossible Substitutions")
print("----------------------")

number_to_compare = min(
    len(sorted_cipher),
    len(sorted_english)
)

for i in range(number_to_compare):

    cipher_code = sorted_cipher[i][0]

    cipher_probability = sorted_cipher[i][1] * 100

    english_letter = sorted_english[i][0]

    english_probability = sorted_english[i][1]

    print(
        cipher_code,
        " -> ",
        english_letter,
        "   Cipher:",
        round(cipher_probability, 2),
        "%",
        "  English:",
        english_probability,
        "%"
    )

#############################################################
## BIGRAM ANALYSIS

bigram_frequency = Sequence_Frequency(cipher, 2)

sorted_bigrams = sorted(
    bigram_frequency.items(),
    key=lambda x: x[1],
    reverse=True
)

print("\nMost Common Cipher Bigrams")
print("--------------------------")

for sequence, count in sorted_bigrams[:10]:

    print(sequence, " -> ", count)

#############################################################

print("\nCommon English Bigrams")
print("----------------------")

for bigram in english_bigrams:

    print(bigram)

#############################################################
## TRIGRAM ANALYSIS

trigram_frequency = Sequence_Frequency(cipher, 3)

sorted_trigrams = sorted(
    trigram_frequency.items(),
    key=lambda x: x[1],
    reverse=True
)

print("\nMost Common Cipher Trigrams")
print("---------------------------")

for sequence, count in sorted_trigrams[:10]:

    print(sequence, " -> ", count)

#############################################################

print("\nCommon English Trigrams")
print("-----------------------")

for trigram in english_trigrams:

    print(trigram)

#############################################################


