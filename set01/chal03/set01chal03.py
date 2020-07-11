# Cryptopals
# Set 01
# Challenge 03

# Single-byte XOR cipher

# Used the pwn tools library to simplify

from pwn import *
from collections import defaultdict
import struct
from decimal import *
from urllib import request

logging.basicConfig(filename='set01chal03.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of challenge')
string1 = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
logging.debug('String 1 is: {}'.format(string1))

logging.debug('Unhexing the string')
unhexStrings = bytes.fromhex(string1)
logging.debug('Unhexed value is: {}'.format(unhexStrings))


def alphacounter(s):
    # Counter(char for char in s.upper() if char.isalpha())
    x = 0
    for byte in s:
        if char.isalpha():
            x += 1
    return x

listBytes = []
for byte in range(254):
    #logging.debug(bytes([byte]))
    xorValue = xor(unhexStrings, bytes([byte]))
    #logging.debug(xorValue)
    listByte = [byte, bytes([byte]), xorValue]
    listBytes.append(listByte)

#print(*listBytes, sep="\n")
#logging.debug(*listBytes, sep="\n")

freqs = defaultdict(int)
total = 0
logging.debug("Counting each character in the text")
with open("pg24397.txt") as f:

    for line in f:
        for char in line:
            char = char.lower()
            #if char.isalpha():
            freqs[char] += 1
            total += 1

logging.debug(freqs)

freqtable = {}

logging.debug("Calculating frequencies")
logging.debug("Making the frequency table")
for key in freqs:
    freqtable[key] = (freqs[key] / total)

logging.debug(freqtable)

print(listBytes[0])
hightotal = 0
highest = []

for x in listBytes:
    #print(x[2])
    total = 0
    print(total)
    print(x)
    for b in x[2]:
        #print(b)
        #print(freqtable.get(chr(b), 0))
        total = freqtable.get(chr(b), 0) + total
    if total > hightotal:
        highest = []
        newhigh = []
        newhigh.append(x)
        newhigh.append(total)
        highest.append(newhigh)
        hightotal = total



print(highest)