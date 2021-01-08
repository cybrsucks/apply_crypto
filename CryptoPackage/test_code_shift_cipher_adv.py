from CryptoPackage import Shift_cipher_adv

plaintext = "nanyangpolytechnic"
plaintext2 = "N4nY4nG PolYt3chn1c"
key_num = 3
key_num2 = 5
key_alpha = "sakurasakurasakura"
key_alpha2 = "rocknrollnrockroll"


def run_test():
    print("-----\nShift Cipher Adv test\n----- ")
    print(Shift_cipher_adv.encrypt_adv(plaintext2, key_num))
    print(Shift_cipher_adv.encrypt_adv(plaintext2, key_num2))
    print(Shift_cipher_adv.decrypt_adv("Q7qb7qJ Srobw6fkq4f", key_num))
    print(Shift_cipher_adv.decrypt_adv("S9sd9sL Utqdy8hms6h", key_num2))


if __name__ == "__main__":
    run_test()
