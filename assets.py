import gmpy2
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad

def write_to_file(data, file):
    with open(f"data/{file}", "w") as f:
        f.write(data)         

def get_file_content(file):
    with open (f"data/{file}", "r") as f:
        str = f.read()
    return str

def encrypt_pt(key, plain_text):
    initial_vector = "00000000000000000000000000000000"
    iv = bytes.fromhex(initial_vector)
    pt = bytes.fromhex(plain_text)

    cipher_encrypt = AES.new(key, AES.MODE_CBC, iv)
    return cipher_encrypt.encrypt(pad(pt, AES.block_size)).hex()

def decrypt_ct(key, ct):
    initial_vector = "00000000000000000000000000000000"
    iv = bytes.fromhex(initial_vector)

    cipher_decrypt = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher_decrypt.decrypt(ct), AES.block_size).hex()

def calc_hash(big, small):
    p = gmpy2.mpz(get_file_content("p.txt"))

    sha2value = str(gmpy2.powmod(big, small, p)).encode('utf-8')
    return hashlib.sha256(sha2value).digest()