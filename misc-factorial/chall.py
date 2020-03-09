import sys
import time
import math
import random
import signal
import itertools
from fractions import gcd
from flag import flag

# Time allowed to complete the challenge (seconds)
DELAY = 10

##
## Handler for the timeout
##
def handler(signum, frame):
   raise Exception("Time is up!\n")


def ord(n, p):
    # highest power or p which divides n!
    tot = 0
    while n != 0:
        n /= p
        tot += n
    return tot
    
def special_fact(mod):
    # prod of all where gcd(n, 10) == 1 and n <= N, result modulo mod
    f, tot = [], 1
    for n in xrange(mod + 1):
        if gcd(n, 10) == 1:
            tot = (tot * n) % mod
        f.append(tot)
    return f

##
## Remove trailing zeros of N!, and return that number modulo "mod"
##                
def g(N, mod):
    facts = special_fact(mod)
    tot, v2, v5 = 1, int(math.log(N, 2)), int(math.log(N, 5))    
    for r, s in itertools.product(xrange(v2 + 1), xrange(v5 + 1)):
        q = 2**r * 5**s
        tot = (tot * facts[(N // q) % mod]) % mod
    b = ord(N, 2) - ord(N, 5)
    tot = (tot * pow(2, b, mod)) % mod
    return tot

##
## N! modulo mod
##
def f(N, mod):
    res = 1
    for i in range(2, N + 1):
        res = (res*i) % mod
    return res

##
## Get a new random integer that is not in the set S
##
def getNewRandom(a, b, S):
    while True:
        r = random.randint(a, b)
        if r not in S:
            break
    S.add(r)
    return r, S

##
##
##
def p(s):
    sys.stdout.write(s)
    sys.stdout.flush()

if __name__== "__main__":
    p("Programming challenge!\n")
    p("----------------------\n")
    p("You have {} seconds to complete the challenge.\n".format(DELAY))
    signal.alarm(DELAY)
    signal.signal(signal.SIGALRM, handler)
    try:
        p("Let n! denote factorial of n, calculated by the product of all integer numbers from 1 to n.\n")
        p("For instance, 5! = 1*2*3*4*5 = 120.\n")
        n = random.randint(6,6)
        p("Then, we have {}! = \n".format(n))
        while True:
            p(">> ")
            res = sys.stdin.readline().strip()
            if res: break
        if math.factorial(n) != int(res):
            p("Sorry, it is not the correct answer, please try again.\n")
            exit(1)
        p("Good, so now we are only interested in the last digits of n!.\n")
        p("Here are a few examples.\n")
        bounds = [
            (4, 4),
            (2, 10),
            (5, 10),
            (10**1, 10**2),
            (10**1, 10**2),
            (10**1, 10**2),
            (10**2, 10**4),
            (10**2, 10**4),
            (10**3, 10**4),
        ]
        for a,b in bounds:
            n = random.randint(a, b)
            p("What is the last digit of {}!\n".format(n))
            while True:
                p(">> ")
                res = sys.stdin.readline().strip()
                if res: break
            if f(n, 10) != int(res):
                p("Sorry, it is not the correct answer, please try again.\n")
                exit(1)
        p("Okay, so there seems to be a lot of zeros...\n")
        p("So now, we remove all the zeros appearing at the end of n! (and only at the end), and consider again the last digits.\n")
        p("For example, the last nonzero digit of 5! is '2', the 2 last nonzero digits of 6! are '72', and the 2 and 3 last nonzero digits of 7! are '04' and '504', respectively.\n")
        ## (min, max, number of digits)
        bounds = [
            (5, 10, 2),
            (5, 10, 2),
            (7, 20, 3),
            (7, 20, 3),
            (8, 30, 4),
            (8, 30, 4),
            #
            (10**1, 10**2, 2),
            (10**1, 10**2, 2),
            (10**1, 10**2, 3),
            (10**1, 10**2, 3),
            (10**1, 10**2, 4),
            (10**1, 10**2, 4),
            #
            (10**2, 10**4, 2),
            (10**2, 10**4, 2),
            (10**2, 10**4, 3),
            (10**2, 10**4, 3),
            (10**2, 10**4, 4),
            (10**2, 10**4, 4),
            #
            (10**4, 10**8, 2),
            (10**4, 10**8, 2),
            (10**4, 10**8, 3),
            (10**4, 10**8, 3),
            (10**4, 10**8, 4),
            (10**4, 10**8, 4),
            #
            (10**8, 10**12, 2),
            (10**8, 10**12, 2),
            (10**8, 10**12, 3),
            (10**8, 10**12, 3),
            (10**8, 10**12, 4),
            (10**8, 10**12, 4),
            #
            (10**12, 10**50, 2),
            (10**12, 10**50, 2),
            (10**12, 10**50, 2),
            (10**12, 10**50, 3),
            (10**12, 10**50, 3),
            (10**12, 10**50, 3),
            (10**12, 10**50, 4),
            (10**12, 10**50, 4),
            (10**12, 10**50, 4),
            (10**12, 10**50, 4),
        ]
        S = set()
        for a,b,d in bounds:
            n, S = getNewRandom(a, b, S)
            p("What are the {} last nonzero digits of {}!\n".format(d, n))
            while True:
                p(">> ")
                res = sys.stdin.readline().strip()
                if res: break
            if g(n, 10**d) != int(res):
                p("Sorry, it is not the correct answer, please try again.\n")
                exit(1)
        p("Congrats! Here is your flag: {}\n".format(flag))
    except Exception as e: 
        p("\nTime is up!\n")
    else:
        sys.exit(0)
