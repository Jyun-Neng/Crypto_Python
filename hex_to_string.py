import binascii
import codecs

h = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
hex = codecs.decode(h, 'hex')	# Convert hex to string.
base = binascii.b2a_base64(hex)	# Convert binary data to ASCII string.
base = str(base, 'utf-8')
hex = str(hex, 'utf-8')
print(hex)	
print(base)