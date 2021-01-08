alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt(plaintext, key):
    ciphertext = ""

    for char in plaintext:
        if char.upper() in alphabet:
            if key > 0:
                num = (alphabet.index(char.upper()) + key) % 26
                if char.isupper():
                    ciphertext += alphabet[num]
                else:
                    ciphertext += alphabet[num].lower()
            else:
                num = (alphabet.index(char.upper()) - key) % 26
                ciphertext += alphabet[num]
        else:
            ciphertext += char
    return ciphertext


# print(encrypt("ALIBABA!@#", 4))


def decrypt(ciphertext, key):
    plaintext = ""

    for char in ciphertext:
        if char.upper() in alphabet:
            if key > 0:
                num = (alphabet.index(char.upper()) - key) % 26
                if char.isupper():
                    plaintext += alphabet[num]
                else:
                    plaintext += alphabet[num].lower()
            else:
                num = (alphabet.index(char) - key) % 26
                plaintext += alphabet[num]
        else:
            plaintext += char
    return plaintext


