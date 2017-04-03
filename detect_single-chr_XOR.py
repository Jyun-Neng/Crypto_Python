'''
One of the 60-character strings in the file has been encrypted by single-character XOR.
Find it.
'''
from bs4 import BeautifulSoup as bs
import requests as rq
import codecs
'''
Use for web file.
'''
url = 'https://cryptopals.com/static/challenge-data/4.txt'
yelp_r = rq.get(url)
text = bs(yelp_r.text, 'html.parser')
cipher_text = ''.join(line for line in text)
cipher_text = cipher_text.splitlines()	# Just include characters.
for line in cipher_text:
	cipher_text = codecs.decode(line, 'hex')
	for k in range(256):
		plain_text = ''.join(chr(k ^ x) for x in cipher_text)
		if plain_text.rstrip('\n').isprintable():
			if ord(plain_text[0]) <= 90 and ord(plain_text[0]) >= 65:	# First chr is upper chr.
				print(chr(k),plain_text)

'''
Use for local file.
'''
cipher_text = open('ciphertext').read().splitlines()	# Just include characters.
for line in cipher_text:	
	cipher_text = codecs.decode(line, 'hex')
	for k in range(256):
		plain_text = ''.join(chr(k ^ x) for x in cipher_text)
		if plain_text.rstrip('\n').isprintable():
			if ord(plain_text[0]) <= 90 and ord(plain_text[0]) >= 65:	# First chr is upper chr.
				print(chr(k),plain_text)	