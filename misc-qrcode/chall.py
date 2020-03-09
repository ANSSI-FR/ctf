import sys
import zlib
import uuid
import base64
import qrcode
import random
import signal
from PIL import Image
from flag import flag

# The challenge image consists of an N*N grid of QRcodes
N = 8

# Time allowed to answer
DELAY = 2

# Size of ONE QRcode
width, height = 290, 290

##
## print with flush
##
def p(s):
	sys.stdout.write(s)
	sys.stdout.flush()

##
## Generate a challenge
##
def newChallenge():
	im = Image.new('RGB', (N*width, N*height))
	L = [ [ random.randint(2**31, 2**32-1) for _ in range(N) ] for _ in range(N) ]

	sum = 0
	for i in range(N):
		for j in range(N):
			sum += L[i][j]
			qr = qrcode.make(L[i][j])
			im.paste( qr, (width*i, height*j) )

	filename = str(uuid.uuid4()) + ".png"
	im.save(filename)
	data = open(filename, "rb").read()
	return base64.encodestring(zlib.compress(data)), sum

##
## Handler for the timeout
##
def handler(signum, frame):
   raise Exception("Time is up!\n")

##
## Read the user answer from stdin, and check
##
def checkAnswer(solution):
	while True:
		p(">> ")
		res = sys.stdin.readline().strip()
		if res: break
	if int(res) != solution:
		p("Wrong, this is incorrect.\n")
	else:
		p("Congrats! Here is your flag: {}\n".format(flag))

if __name__== "__main__":
	p("Programming challenge\n")
	p("---------------------\n")
	p("I will send you a PNG image compressed by zlib encoded in base64 that contains {} encoded numbers.\n".format(N*N))
	p("The expected answer is the sum of all the numbers (in decimal).\n")
	p("You have {} seconds.\n".format(DELAY))
	p("Are you ready? [Y/N]\n")
	while True:
		p(">> ")
		res = sys.stdin.readline().strip()
		if res: break
	if res == "Y" or res == 'y':
		# Generate the challenge
		chall, solution = newChallenge()
		# Send the challenge
		p(chall.decode())
		# Get and check answer in less than 5 seconds, otherwise, exit
		p("What is you answer?\n")
		#
		signal.alarm(DELAY)
		signal.signal(signal.SIGALRM, handler)
		try:
			checkAnswer(solution)
		except Exception as e: 
			p("\nTime is up!\n")
	else:
		sys.exit(0)
