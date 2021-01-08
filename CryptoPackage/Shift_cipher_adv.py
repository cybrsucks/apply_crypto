alphabet2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='


def encrypt_adv(plaintext, key, alphabet_list=alphabet2):
    ciphertext = ""
    for char in plaintext:
        if char in alphabet_list:
            if key > 0:
                num = (alphabet_list.index(char) + key) % len(alphabet_list)
                ciphertext += alphabet_list[num]
            else:
                num = (alphabet_list.index(char) - key) % len(alphabet_list)
                ciphertext += alphabet_list[num]
        else:
            ciphertext += char
    return ciphertext


def decrypt_adv(ciphertext, key, alphabet_list=alphabet2):
    plaintext = ""
    for char in ciphertext:
        if char in alphabet_list:
            if key > 0:
                num = (alphabet_list.index(char) - key) % len(alphabet_list)
                plaintext += alphabet_list[num]
            else:
                num = (alphabet_list.index(char) + key) % len(alphabet_list)
                plaintext += alphabet_list[num]
        else:
            plaintext += char
    return plaintext

