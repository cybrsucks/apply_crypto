from Crypto.Cipher import AES
import Crypto.Random
import Crypto.Cipher
from Crypto.Util.Padding import pad, unpad

# Cipher modes: ECB, CBC, CFB and OFB
# Key sizes: 128, 192 and 256 bits

def get_random_key(key_size):
    if key_size == 128:
        return Crypto.Random.get_random_bytes(16)
    elif key_size == 192:
        return Crypto.Random.get_random_bytes(24)
    elif key_size == 256:
        return Crypto.Random.get_random_bytes(32)

# ECB start
def encrypt_ECB(key, plaintext_utf8):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext_utf8, AES.block_size))
    return ciphertext

def decrypt_ECB(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    decryptedtext_utf = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decryptedtext_utf
# ECB end
# CBC start
def encrypt_CBC(key, plaintext_utf8):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext_utf8, AES.block_size))
    return cipher.iv, ciphertext

def decrypt_CBC(key, ciphertext, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decryptedtext_utf = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decryptedtext_utf
# CBC end
# CFB start
def encrypt_CFB(key, plaintext_utf8):
    cipher = AES.new(key, AES.MODE_CFB)
    ciphertext = cipher.encrypt(pad(plaintext_utf8, AES.block_size))
    return cipher.iv, ciphertext

def decrypt_CFB(key, ciphertext, iv):
    cipher = AES.new(key, AES.MODE_CFB, iv)
    decryptedtext_utf = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decryptedtext_utf
# CFB end
# OFB start
def encrypt_OFB(key, plaintext_utf8):
    cipher = AES.new(key, AES.MODE_OFB)
    ciphertext = cipher.encrypt(pad(plaintext_utf8, AES.block_size))
    return cipher.iv, ciphertext

def decrypt_OFB(key, ciphertext, iv):
    cipher = AES.new(key, AES.MODE_OFB, iv)
    decryptedtext_utf = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decryptedtext_utf
# OFB end
