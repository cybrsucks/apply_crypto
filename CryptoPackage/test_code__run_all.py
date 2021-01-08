from CryptoPackage import test_code_vernam_cipher, test_code_rail_fence, test_code_shift_cipher_adv, test_code_shift_cipher, test_code_AES


def run_test():
    test_code_shift_cipher.run_test()
    test_code_shift_cipher_adv.run_test()
    test_code_rail_fence.run_test()
    test_code_vernam_cipher.run_test()
    test_code_AES.run_test()


if __name__ == "__main__":
    run_test()
