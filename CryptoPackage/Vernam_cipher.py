alphabets = 'abcdefghijklmnopqrstuvwxyz'


def encrypt(plaintext, key):
    ciphertext = ''
    plaintext = plaintext.lower()
    key = key.lower()
    if len(key) <= len(plaintext):
        for count, char in enumerate(plaintext):
            i = j = 0
            if char in alphabets:
                i = alphabets.index(char)
                # i and j is the index number of the character A=1; B=2; C=3, etc.
                key_letter = key[count]
                # print(key_letter)
                if key_letter in alphabets:
                    j = alphabets.index(key_letter)
                    encrypt = i + j
                    encrypt %= 26
                    new_letter = alphabets[encrypt]
                else:
                    new_letter = alphabets[i]
            else:
                new_letter = alphabets[j]

            ciphertext += new_letter
        return ciphertext


def decrypt(ciphertext, key):
    plaintext = ''
    ciphertext = ciphertext.lower()
    key = key.lower()
    if len(key) <= len(ciphertext):
        for count, char in enumerate(ciphertext):
            i = j = 0
            if char in alphabets:
                i = alphabets.index(char)
                # i and j is the index number of the character A=1; B=2; C=3, etc.
                key_letter = key[count]
                if key_letter in alphabets:
                    j = alphabets.index(key_letter)
                    # temp_letter = i + 26
                    # result_letter = temp_letter - j
                    result_letter = i + 26 - j
                    if result_letter < 26:
                        new_letter = alphabets[result_letter]
                    else:
                        new_letter = alphabets[i - j]
                else:
                    new_letter = alphabets[i - j]
            else:
                new_letter = alphabets[i - j]

            plaintext += new_letter
        return plaintext


# print(encrypt('peace', 'world'))
# print(encrypt('cool', 'bean'))
# print(decrypt('lsrnh', 'world'))
# print(decrypt('dsoy', 'bean'))
