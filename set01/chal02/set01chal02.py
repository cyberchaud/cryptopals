# Cryptopals
# Set 01
# Challenge 02

# Fixed XOR
# XOR 2 equal length strings and compare XOR Combination with res

# Used the pwn tools library to simplify

from pwn import *

logging.basicConfig(filename='set01chal02.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of challenge')
string1 = '1c0111001f010100061a024b53535009181c'
string2 = '686974207468652062756c6c277320657965'
expectedresult = '746865206b696420646f6e277420706c6179'
logging.debug('String 1 is: {}'.format(string1))
logging.debug('String 2 is: {}'.format(string2))

logging.debug('XORing the strings')
xorResult = xor(bytes.fromhex(string1), bytes.fromhex(string2)).hex()
logging.debug('Xord value: {}'.format(xorResult))

assert xorResult == expectedresult
