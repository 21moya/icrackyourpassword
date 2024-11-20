import os
import gmpy2
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad     

BASE_DIR = os.path.dirname(os.path.abspath(__file__)).split("\\src")[0]
INITIAL_VECTOR = "00000000000000000000000000000000"
IV = bytes.fromhex(INITIAL_VECTOR)

def get_file_content(file):
    with open (os.path.join(BASE_DIR, "data", file), "r") as f:
        str = f.read()
    return str

def encrypt_pt(key, plain_text):
    pt = bytes.fromhex(plain_text)

    cipher_encrypt = AES.new(key, AES.MODE_CBC, IV)
    return cipher_encrypt.encrypt(pad(pt, AES.block_size)).hex()

def decrypt_ct(key, ct):
    cipher_decrypt = AES.new(key, AES.MODE_CBC, IV)
    return unpad(cipher_decrypt.decrypt(ct), AES.block_size).hex()

def calc_hash(big, small):
    p = gmpy2.mpz(get_file_content("p.txt"))
    sha2value = str(gmpy2.powmod(big, small, p)).encode('utf-8')
    return hashlib.sha256(sha2value).digest()