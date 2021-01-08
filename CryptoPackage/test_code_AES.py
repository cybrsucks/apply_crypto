from CryptoPackage import AES_run


def run_test():
    plaintext = "nanyangpolytechnic".encode("utf-8")
    key = AES_run.get_random_key(128)
    print(key, plaintext)

    print("\nEncrypt ECB")
    ciphertext = AES_run.encrypt_ECB(key, plaintext)
    print("Ciphertext: {}".format(f"{ciphertext}"[2:-1]))

    print("\nDecrypt ECB")
    plaintext2 = AES_run.decrypt_ECB(key, ciphertext)
    print("Plaintext: {}".format(plaintext2))


    print("\nEncrypt CBC")
    iv, ciphertext = AES_run.encrypt_CBC(key, plaintext)
    print("IV: {}".format(iv))
    print("Ciphertext: {}".format(f"{ciphertext}"[2:-1]))

    print("\nDecrypt CBC")
    plaintext2 = AES_run.decrypt_CBC(key, ciphertext, iv)
    print("Plaintext: {}".format(plaintext2))


    print("\nEncrypt CFB")
    iv, ciphertext = AES_run.encrypt_CFB(key, plaintext)
    print("IV: {}".format(iv))
    print("Ciphertext: {}".format(f"{ciphertext}"[2:-1]))

    print("\nDecrypt CFB")
    plaintext2 = AES_run.decrypt_CFB(key, ciphertext, iv)
    print("Plaintext: {}".format(plaintext2))


    print("\nEncrypt OFB")
    iv, ciphertext = AES_run.encrypt_OFB(key, plaintext)
    print("IV: {}".format(iv))
    print("Ciphertext: {}".format(f"{ciphertext}"[2:-1]))

    print("\nDecrypt OFB")
    plaintext2 = AES_run.decrypt_OFB(key, ciphertext, iv)
    print("Plaintext: {}".format(plaintext2))


if __name__ == "__main__":
    run_test()
