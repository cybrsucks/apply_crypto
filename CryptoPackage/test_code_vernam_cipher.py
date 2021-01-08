from CryptoPackage import Vernam_cipher

plaintext = "nanyangpolytechnic"
plaintext2 = "N4nY4nG PolYt3chn1c"
key_num = 3
key_num2 = 5
key_alpha = "sakurasakurasakura"
key_alpha2 = "rocknrollnrockroll"


def run_test():
    print("-----\nVernam Cipher test\n----- ")
    print(Vernam_cipher.encrypt(plaintext, key_alpha))
    print(Vernam_cipher.encrypt(plaintext, key_alpha2))
    print(Vernam_cipher.decrypt("faxsrnypyfptwcrhzc", key_alpha))
    print(Vernam_cipher.decrypt("eopineuazyphgmybtn", key_alpha2))


if __name__ == "__main__":
    run_test()
