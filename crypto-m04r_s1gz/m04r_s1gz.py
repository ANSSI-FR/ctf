#!/usr/bin/python3 -u
from Crypto.PublicKey import RSA
import secrets
import signal
import sys


class SecureSigner():
    def __init__(self):
        self.private_key = RSA.generate(2048)
        self.e, self.n = self.private_key.e, self.private_key.n

    def sign(self, message):
        return self.private_key.sign(m, None)

    def verify(self, message, signature):
        return self.private_key.verify(message, (signature,))


if __name__ == '__main__':
    s = SecureSigner()

    print("Can you beat us and forge a signature in less than 60 seconds?")
    signal.alarm(60)

    print("Here are your parameters:\n - modulus n: {:d}\n - public exponent e: {:d}".format(s.n, s.e))

    while True:
        message = input("Please enter a number to sign (or anything else to stop): ")
        try:
            m = int(message, 10)
        except ValueError:
            break
        signature = s.sign(m)
        print("Signature: {:d}".format(signature[0]))
    
    challenge = secrets.randbelow(2**32)
    print("Here is your challenge: {:d}".format(challenge))
    
    signature = input("Enter the signature of the challenge: ")
    try:
        sig = int(signature, 10)
    except ValueError:
        print("[-] Wrong signature format!")
        sys.exit(-1)
    
    if s.verify(challenge, sig):
        with open("flag", "rb") as f:
            flag = f.read()
            signal.alarm(0)
            print("[+] Here is your flag, fellow signer: {:s}".format(flag.decode()))
    else:
        print("[-] Try again :(")
        sys.exit(-1)
