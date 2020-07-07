# Cryptopals
# Set 01
# Challenge 02

# Fixed XOR
# XOR 2 equal length strings and compare XOR Combination with res

import base64
import logging
import binascii
from bitstring import BitArray

def expectedResult(s):
    res = '746865206b696420646f6e277420706c6179'
    logging.debug('Result string is {}'.format(res))
    logging.debug('S string is {}'.format(s))
    return (s == res)


def stringtobin(s):
    a = BitArray(hex=s)
    return a.bin

def xor2bins(b1, b2):
    bin1 = int(b1, 2)
    bin2 = int(b2, 2)
    xor = bin1 ^ bin2

    return hex(xor)[2:]



logging.basicConfig(filename='set01chal02.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of challenge')
string1 = '1c0111001f010100061a024b53535009181c'
string2 = '686974207468652062756c6c277320657965'
res = '746865206b696420646f6e277420706c6179'
logging.debug('Input string is {}'.format(string1))
logging.debug('Converting string to binary')

binarystring1 = stringtobin(string1)
binarystring2 = stringtobin(string2)

logging.debug('String1 in binary is: {}'.format(binarystring1))
logging.debug('String2 in binary is: {}'.format(binarystring2))

logging.debug('XORing the strings')
xorresult = xor2bins(binarystring1, binarystring2)

logging.debug('The result XOR is {}:'.format(xorresult))

print(expectedResult(xorresult))

logging.debug('End of challenge')

