from CryptoPackage import Rail_fence

plaintext = "nanyangpolytechnic"
plaintext2 = "N4nY4nG PolYt3chn1c"
key_num = 3
key_num2 = 5
key_alpha = "sakurasakurasakura"
key_alpha2 = "rocknrollnrockroll"


def run_test():
    print("-----\nRail Fence test\n----- ")
    print(Rail_fence.encryptRailFence(plaintext, key_num))
    print(Rail_fence.encryptRailFence(plaintext, key_num2))
    print(Rail_fence.decryptRailFence("naptnayn oyehinglcc", key_num))
    print(Rail_fence.decryptRailFence("npna ohinglccynyeat", key_num2))


if __name__ == "__main__":
    run_test()
