from flask import Flask, render_template, request
import base64

app = Flask(__name__)

def xor_cipher(text, key):
    return ''.join([chr(ord(c) ^ key) for c in text])

def unicode_shift(text, shift):
    return ''.join([chr((ord(c)+shift)%0x110000) for c in text])

def multiplicative_cipher(text, key):
    return ''.join([chr((ord(c)*key)%256) for c in text])

def substitution_cipher(text, alphabet="ZYXWVUTSRQPONMLKJIHGFEDCBA"):
    base = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for c in text.upper():
        if c in base:
            result += alphabet[base.index(c)]
        else:
            result += c
    return result

def reverse_xor_cipher(text, key):
    reversed_text = text[::-1]
    return ''.join([chr(ord(c) ^ key) for c in reversed_text])

def caesar_cipher(text, shift=3):
    result = ""
    for c in text:
        if c.isalpha():
            offset = 65 if c.isupper() else 97
            result += chr((ord(c)-offset+shift)%26 + offset)
        else:
            result += c
    return result

def rot13(text):
    return caesar_cipher(text, 13)

def base32_encode(text):
    return base64.b32encode(text.encode()).decode()

def base32_decode(text):
    return base64.b32decode(text.encode()).decode()

def base64_encode(text):
    return base64.b64encode(text.encode()).decode()

def base64_decode(text):
    return base64.b64decode(text.encode()).decode()

def hex_encode(text):
    return text.encode().hex()

def hex_decode(text):
    return bytes.fromhex(text).decode()

def binary_encode(text):
    return ' '.join(format(ord(c),'08b') for c in text)

def binary_decode(text):
    return ''.join([chr(int(b,2)) for b in text.split()])

def url_encode(text):
    from urllib.parse import quote
    return quote(text)

def url_decode(text):
    from urllib.parse import unquote
    return unquote(text)

def custom_formula_encode(text, formula="(ord(c)+3)%256"):
    result = ""
    for c in text:
        result += chr(eval(formula))
    return result

def custom_formula_decode(text, formula="(ord(c)-3)%256"):
    result = ""
    for c in text:
        result += chr(eval(formula))
    return result

def encode_text(text, method, key=3, formula="(ord(c)+3)%256"):
    if method == "Base64":
        return base64_encode(text)
    elif method == "Base64 Decode":
        return base64_decode(text)
    elif method == "Base32":
        return base32_encode(text)
    elif method == "Base32 Decode":
        return base32_decode(text)
    elif method == "Hex":
        return hex_encode(text)
    elif method == "Hex Decode":
        return hex_decode(text)
    elif method == "Binary":
        return binary_encode(text)
    elif method == "Binary Decode":
        return binary_decode(text)
    elif method == "ROT13":
        return rot13(text)
    elif method == "Caesar Cipher":
        return caesar_cipher(text, key)
    elif method == "XOR":
        return xor_cipher(text, key)
    elif method == "Unicode Shift":
        return unicode_shift(text, key)
    elif method == "Multiplicative":
        return multiplicative_cipher(text, key)
    elif method == "Substitution":
        return substitution_cipher(text)
    elif method == "Reverse XOR":
        return reverse_xor_cipher(text, key)
    elif method == "URL Encode":
        return url_encode(text)
    elif method == "URL Decode":
        return url_decode(text)
    elif method == "Custom Encode":
        return custom_formula_encode(text, formula)
    elif method == "Custom Decode":
        return custom_formula_decode(text, formula)
    return text

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        text = request.form.get("text", "")
        method = request.form.get("method", "Base64")
        key = int(request.form.get("key", 3) or 3)
        formula = request.form.get("formula", "(ord(c)+3)%256")
        result = encode_text(text, method, key, formula)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
