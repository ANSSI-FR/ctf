import os
import sys
import bitarray
import random

N = 64

def state2str(state):
	b = bitarray.bitarray(state)
	return b.tobytes().hex()

def filtered(state):
	b  = 0
	b ^= state[0]*state[N//4]
	b ^= state[0]*state[2*N//4]*state[3*N//4]
	b ^= state[N//4]*state[2*N//4]*state[3*N//4]
	b ^= state[N//4]*state[2*N//4]
	b ^= state[N//4]*state[3*N//4]
	b ^= state[N//4]
	return b

def clock(state):
	b = filtered(state)
	tmp = state[0] ^ state[1] ^ state[3] ^ state[4]
	state = state[1:] + [tmp]
	return b, state

def encrypt(file):
	state = [ random.getrandbits(1) for _ in range(N) ]
	sys.stderr.write("[+] Encrypting file: {}\n".format(file))
	sys.stderr.write("[+] Random initial state: 0x{}\n".format(state2str(state)))

	data = open(file, "rb").read()
	bIn = bitarray.bitarray()
	bIn.frombytes(data)

	bOut = bitarray.bitarray()
	for b in bIn:
		bit, state = clock(state)
		bOut.append(bit^b)

	sys.stdout.buffer.write(bOut.tobytes())
	sys.stderr.write("[+] Done\n")

def decrypt(file, state):
	state = int(state, 16)
	state = [ (state>>i)&1 for i in range(N-1, -1, -1) ]

	sys.stderr.write("[+] Decrypting file: {}\n".format(file))
	sys.stderr.write("[+] Using initial state: 0x{}\n".format(state2str(state)))

	data = open(file, "rb").read()
	bIn = bitarray.bitarray()
	bIn.frombytes(data)

	bOut = bitarray.bitarray()
	for b in bIn:
		bit, state = clock(state)
		bOut.append(bit^b)

	sys.stdout.buffer.write(bOut.tobytes())

def usage():
	print ("Usage: ")
	print ("\tEncrypt: ./%s <file>" % sys.argv[0])
	print ("\tDecrypt: ./%s <file> <initial state (hex)>" % sys.argv[0])

if __name__== "__main__":
	if   len(sys.argv) == 1: usage()
	elif len(sys.argv) == 2: encrypt(sys.argv[1])              # encrypt
	elif len(sys.argv) == 3: decrypt(sys.argv[1], sys.argv[2]) # decrypt
	else:                    usage()
