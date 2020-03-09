# -*- coding: utf-8 -*-

import re
import string
import unicodedata

CHARSET = string.ascii_uppercase + string.digits # ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

def strip_text(plaintext):
	res = ""
	for x in plaintext.upper():
		if not x in CHARSET: continue
		res += x
	return res

def encrypt(plaintext, key):
	key_length = len(key)
	ciphertext = ''
	for i in range(len(plaintext)):
		id_p = CHARSET.find(plaintext[i])
		id_k = CHARSET.find(key[i % key_length])
		id_c = (id_p + id_k) % len(CHARSET)
		ciphertext += CHARSET[id_c]
	return ciphertext

#########################################
############ Generation part ############
#########################################

texte = open("plaintext.txt", "r").read()
texte = unicodedata.normalize('NFD', texte).encode('ascii', 'ignore')
texte = texte.decode()
texte = strip_text(texte)
ctxt = encrypt(texte, "L33TV1G3NER3")

group_len = 5
ctxt = ' '.join(ctxt[i:i+group_len] for i in range(0, len(ctxt), group_len))
ngroups = 10
length = ngroups*group_len+ngroups
ctxt = '\n'.join(ctxt[i:i+length] for i in range(0, len(ctxt), length))

open("ciphertext.txt", "w").write(ctxt+"\n")
del ctxt

## flag: lh_l33tv1g3ner3_f0rth3w1n
## Commentaire: le flag est à soumettre en minuscules
