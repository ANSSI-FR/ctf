import sys
import binascii
import random
import string
import hashlib
from random import randint
from flag import flag

N = 8

rol = lambda val, r_bits, max_bits:                          \
  (val << r_bits%max_bits) & (2**max_bits-1) |               \
  ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))

def p(s):
	sys.stdout.write(s)
	sys.stdout.flush()

def check(N, S):
	assert len(S) == 2**N-1, "Error: the sequence should be of length {}".format(2**N-1)
	rotations = [ randint(0, N-1) for _ in range(2**N-1) ]
	SS = [ rol(S[i], rotations[i], N) for i in range(2**N-1) ]
	values = [0]
	tmp = 0
	for i in range(2**N-1):
		tmp ^= SS[i]
		values += [tmp]
	return len(set(values)) == 2**N

def anti_bruteforce_PoW(difficulty):
	randstr = ''.join(random.choice(string.ascii_letters) for _ in range(32))
	print("Enter a string S such that the {} most signicant bits".format(difficulty))
	print("of sha256(P||S) are zeros, with the prefix P is defined as");
	print("P = {}".format(randstr))
	S = input(">> ")
	randstr += S
	m = hashlib.sha256()
	m.update(randstr.encode())
	h = m.digest()
	bits = "{:0256b}".format(int(h.hex(), 16))
	return bits[:difficulty] == "0"*difficulty

'''
def solve_PoW(prefix, difficulty):
	while True:
		suffix = ''.join(random.choice(string.ascii_letters) for _ in range(32)) 
		randstr = prefix + suffix
		m = hashlib.sha256()
		m.update(randstr.encode())
		h = m.digest()
		bits = "{:0256b}".format(int(h.hex(), 16))
		if bits[:difficulty] == "0"*difficulty:
			return suffix
			break
'''

if __name__== "__main__":

	## Welcome
	p("Algorithmic challenge\n")
	p("---------------------\n")
	assert (N!=0) and ((N&(N-1)) == 0), "Error: N must be a power of 2."

	## Anti-brutefoce
	p("Before starting the actual challenge, we limit the access by a proof-of-work mechanism.\n")
	if not anti_bruteforce_PoW(18):
		p("Error: Please retry solving the PoW.\n")
		exit(1)

	## Actual challenge
	p("You passed the PoW verification!\n")
	p("You can now attempt to solve the challenge:\n")
	while True:
		s = input(">>> ")
		try:
			s = list(binascii.unhexlify(s))
			if len(s) == 2**N - 1: break
		except:
			pass

	## Check of the solution
	if check(N, s):
		p("Congrats!! Here is the flag: {}\n".format(flag))
	else:
		p("Not Good.\n")
