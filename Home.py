from flask import Flask, render_template, request
from CryptoPackage import Rail_fence, Shift_cipher_adv, Vernam_cipher, AES_run, Shift_cipher

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about_me.html')


@app.route("/documentation")
def document():
    return render_template('documentation.html')


@app.route("/need_for_security")
def nfs():
    return render_template('need_for_security.html')


@app.route("/trusted_systems_and_reference_monitor")
def tsrf():
    return render_template('trusted_systems_and_ref_monitor.html')


@app.route("/security_models")
def sm():
    return render_template('security_models.html')


@app.route("/security_management_practices")
def smp():
    return render_template('security_management_pract.html')


@app.route("/types_of_attacks")
def toa():
    return render_template('types_of_attacks.html')


@app.route("/shift_cipher", methods=['GET', 'POST'])
def shiftcipher():
    if request.method == "POST":
        try:
            enplaintext = request.form["encrypt_plaintext"]
            enkey = int(request.form["encrypt_key"])
            if enplaintext != "" and enkey != "":
                ciphertext = Shift_cipher.encrypt(enplaintext, enkey)
        except KeyError:
            ciphertext = ""
        try:
            deciphertext = request.form["decrypt_ciphertext"]
            dekey = int(request.form["decrypt_key"])
            if deciphertext != "" and dekey != "":
                plaintext = Shift_cipher.decrypt(deciphertext, dekey)
        except KeyError:
            plaintext = ""

        return render_template('shift_cipher.html', plaintext=plaintext, ciphertext=ciphertext)

    return render_template("shift_cipher.html")


@app.route("/shift_cipher_more", methods=['GET', 'POST'])
def shiftcipheradv():
    if request.method == "POST":
        try:
            enplaintext = request.form["encrypt_plaintext"]
            enkey = int(request.form["encrypt_key"])
            alphabet_list = request.form["alphabet_list"]
            if enplaintext != "" and enkey != "":
                ciphertext = Shift_cipher_adv.encrypt_adv(enplaintext, enkey, alphabet_list)
        except KeyError:
            ciphertext = ""
        try:
            deciphertext = request.form["decrypt_ciphertext"]
            dekey = int(request.form["decrypt_key"])
            alphabet_list = request.form["alphabet_list"]
            if deciphertext != "" and dekey != "":
                plaintext = Shift_cipher_adv.decrypt_adv(deciphertext, dekey, alphabet_list)
        except KeyError:
            plaintext = ""

        return render_template('shift_cipher_adv.html', plaintext=plaintext, ciphertext=ciphertext)

    return render_template("shift_cipher_adv.html")


@app.route("/rail_fence", methods=['GET', 'POST'])
def railfence():
    if request.method == "POST":
        try:
            enplaintext = request.form["encrypt_plaintext"]
            enkey = int(request.form["encrypt_key"])
            if enplaintext != "" and enkey != "":
                ciphertext = Rail_fence.encryptRailFence(enplaintext, enkey)
        except KeyError:
            ciphertext = ""
        try:
            deciphertext = request.form["decrypt_ciphertext"]
            dekey = int(request.form["decrypt_key"])
            if deciphertext != "" and dekey != "":
                plaintext = Rail_fence.decryptRailFence(deciphertext, dekey)
        except KeyError:
            plaintext = ""

        return render_template('rail_fence.html', plaintext=plaintext, ciphertext=ciphertext)

    return render_template("rail_fence.html")


@app.route("/vernam_cipher", methods=['GET', 'POST'])
def vernamcipher():
    if request.method == "POST":
        try:
            enplaintext = request.form["encrypt_plaintext"]
            enkey = request.form["encrypt_key"]
            if enplaintext != "" and enkey != "":
                ciphertext = Vernam_cipher.encrypt(enplaintext, enkey)
        except KeyError:
            ciphertext = ""
        try:
            deciphertext = request.form["decrypt_ciphertext"]
            dekey = request.form["decrypt_key"]
            if deciphertext != "" and dekey != "":
                plaintext = Vernam_cipher.decrypt(deciphertext, dekey)
        except KeyError:
            plaintext = ""

        return render_template('vernam_cipher.html', plaintext=plaintext, ciphertext=ciphertext)

    return render_template("vernam_cipher.html")


@app.route("/AES_Symmetric_Algorithms", methods=['GET', 'POST'])
def AES():
    if request.method == "POST":
        try:
            enplaintext = request.form["encrypt_plaintext"]
            option_mode = request.form["cipher_mode"]
            keysize = int(request.form["key_size"])
            key = AES_run.get_random_key(keysize)

            if enplaintext != "":
                if option_mode == "ECB":
                    encryptedtext_string = AES_run.encrypt_ECB(key, enplaintext.encode("utf8"))
                    encryptedtext_string = f"{encryptedtext_string}"[2:-1]
                    iv = ''
                elif option_mode == "CBC":
                    iv, encryptedtext_string = AES_run.encrypt_CBC(key, enplaintext.encode("utf8"))
                    iv = f"{iv}"[2:-1]
                    encryptedtext_string = f"{encryptedtext_string}"[2:-1]
                elif option_mode == "CFB":
                    iv, encryptedtext_string = AES_run.encrypt_CFB(key, enplaintext.encode("utf8"))
                    iv = f"{iv}"[2:-1]
                    encryptedtext_string = f"{encryptedtext_string}"[2:-1]
                elif option_mode == "OFB":
                    iv, encryptedtext_string = AES_run.encrypt_OFB(key, enplaintext.encode("utf8"))
                    iv = f"{iv}"[2:-1]
                    encryptedtext_string = f"{encryptedtext_string}"[2:-1]
                key = f"{key}"[2:-1]
        except KeyError:
            iv = ""
            encryptedtext_string = ""
        try:
            deciphertext = request.form["decrypt_ciphertext"]
            iv = request.form["decrypt_key"]
            option_mode = request.form["cipher_mode"]
            keyinput = request.form["key_input"]
            try:
                key = eval("b\"%s\"" % keyinput)
            except:
                key = eval("b\'%s\'" % keyinput)
            if deciphertext != "" or key != "":
                if option_mode == "ECB":
                    display = False
                    iv = ''
                    try:
                        deciphertext = eval("b\"%s\"" % deciphertext)
                    except:
                        deciphertext = eval("b'%s'" % deciphertext)
                    decryptedtext_string = AES_run.decrypt_ECB(key, deciphertext)
                    decryptedtext_string = f"{decryptedtext_string}"[2:-1]  # Run this to convert b'something' to 'something
                elif option_mode == "CBC":
                    try:
                        iv = eval("b\"%s\"" % iv)
                    except:
                        iv = eval("b'%s'" % iv)  # Run this to convert 'something' to b'something'
                    try:
                        deciphertext = eval("b\"%s\"" % deciphertext)
                    except:
                        deciphertext = eval("b'%s'" % deciphertext)
                    decryptedtext_string = AES_run.decrypt_CBC(key, deciphertext, iv)
                    decryptedtext_string = f"{decryptedtext_string}"[2:-1]  # Run this to convert b'something' to 'something
                elif option_mode == "CFB":
                    try:
                        iv = eval("b\"%s\"" % iv)
                    except:
                        iv = eval("b'%s'" % iv)
                    try:
                        deciphertext = eval("b\"%s\"" % deciphertext)
                    except:
                        deciphertext = eval("b'%s'" % deciphertext)
                    decryptedtext_string = AES_run.decrypt_CFB(key, deciphertext, iv)
                    decryptedtext_string = f"{decryptedtext_string}"[2:-1]  # Run this to convert b'something' to 'something
                elif option_mode == "OFB":
                    try:
                        iv = eval("b\"%s\"" % iv)
                    except:
                        iv = eval("b'%s'" % iv)
                    try:
                        deciphertext = eval("b\"%s\"" % deciphertext)
                    except:
                        deciphertext = eval("b'%s'" % deciphertext)
                    decryptedtext_string = AES_run.decrypt_OFB(key, deciphertext, iv)
                    decryptedtext_string = f"{decryptedtext_string}"[2:-1]  # Run this to convert b'something' to 'something
                iv = f"{iv}"[2:-1]
                key = f"{key}"[2:-1]
        except KeyError:
            decryptedtext_string = ""

        return render_template('AES_Symm_Algo.html', plaintext=decryptedtext_string, ciphertext=encryptedtext_string,
                               iv=iv, key=key)

    return render_template("AES_Symm_Algo.html")


if __name__ == '__main__':
    app.run(debug=True)

# plaintext plaintext plaintext plaintext plaintext CFB 256
