#!/usr/bin/python3 -u
from binascii import hexlify
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.backends import default_backend
backend = default_backend()

def derive(secret):
    # Derive the secret so we get key and IV material for AES
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=48,
        salt=secret,
        iterations=100000,
        backend=backend
    )
    return kdf.derive(secret)

def encrypt(key, iv, aad, data):
    aesgcm = AESGCM(key)
    ct = aesgcm.encrypt(iv, data, aad)
    return ct

if __name__ == '__main__':
    # First, retrieve the secret
    with open('key', 'rb') as f:
        secret = f.read(32)

    derived = derive(secret)
    key, iv, aad = derived[:16], derived[16:32], derived[32:]

    print("Welcome to our state-of-the-art encryption service!\nWe use PBKDF2 and AES-GCM!")
    with open('flag', 'rb') as f:
        data = f.read()

    flag = encrypt(key, iv, aad, data)
    print("As an example, here is the encrypted flag: {:s}\n".format(hexlify(flag).decode()))

    data = input("Now, enter your text: ")
    userct = encrypt(key, iv, aad, data.encode('utf-8'))
    print("Here is your ciphertext: {:s}\n".format(hexlify(userct).decode()))
