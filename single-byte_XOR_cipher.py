'''
The hex encoded string:
1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
has been XOR'd against a single character. 
Find the key, decrypt the message.
'''
import codecs
import binascii

encoded = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
encoded = codecs.decode(encoded, 'hex')
for k in range(256):
	decoded = ''.join(chr(k ^ i) for i in encoded)
	if decoded.isprintable():
		print(chr(k), decoded)