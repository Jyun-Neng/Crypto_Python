from operator import xor

hex1 = 0x1c0111001f010100061a024b53535009181c
hex2 = 0x686974207468652062756c6c277320657965

hex3 = hex(xor(hex1, hex2))
print(hex3)