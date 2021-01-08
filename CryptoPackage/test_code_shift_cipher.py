from CryptoPackage import Shift_cipher

plaintext = "nanyangpolytechnic"
plaintext2 = "N4nY4nG PolYt3chn1c"
key_num = 3
key_num2 = 5
key_alpha = "sakurasakurasakura"
key_alpha2 = "rocknrollnrockroll"


def run_test():
    print("Shift Cipher test\n----- ")
    print(Shift_cipher.encrypt(plaintext, key_num))
    print(Shift_cipher.encrypt(plaintext, key_num2))
    print(Shift_cipher.decrypt("qdqbdqj srobwhfkqlf", key_num))
    print(Shift_cipher.decrypt("sfsdfsl utqdyjhmsnh", key_num2))


if __name__ == "__main__":
    run_test()
