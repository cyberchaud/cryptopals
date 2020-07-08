# Cryptopals
# Set 01
# Challenge 03

# Single-byte XOR cipher
# Hex encoded string has been XORd against a single character.
# Tip - Make a scoring system for English plaintext and find the highest score and choose the one with the best output.

from bitstring import BitArray

import logging
import base64
import binascii

def stringtobin(s):
    a = BitArray(hex=s)
    return a.bin

def xor2bins(key, str):
    #bin1 = int(b1, 2)
    #bin2 = int(b2, 2)
    returnbit = ''
    for bit in str:
        returnbit += bit
        #xor = bin1 ^ bin2
    return returnbit
    #return hex(xor)[2:]

def hextoascii(s):
    logging.debug("Inside hextoBase64")
    logging.debug("Value of s is: {}".format(s))
    return binascii.unhexlify(s)

logging.basicConfig(filename='set01chal03.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of challenge')

ciphertext = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

print(bytes.fromhex(ciphertext))
bytesciphertext = bytes.fromhex(ciphertext)
logging.debug('The encoded string is: {}'.format(bytesciphertext))

binstring = stringtobin(ciphertext)

logging.debug('The bin value of the ciphertext is: {}'.format(binstring))

def xorres(key, string):
    x, upper = 0, len(key) - 1
    xresult = ''
    for bit in string:
        #print(str(bit), str(x), str(key), str(int(bit) ^ int(key[x])))
        if x == upper:
            x = 0
        else:
            x += 1
        xresult += str(int(bit) ^ int(key[x]))
        #logging.debug('The xresult is: {}'.format(xresult))
    return xresult

logging.debug('The ciphertext is: {}'.format(ciphertext))

listResults = []
for i in range(0, 255):
        #print(i)
        key = format(i, 'b')
        listResults.append(xorres(key, binstring))
        #logging.debug('The bin xor value is: {}'.format(result))

def bintoByteArray(b):
    rList = []
    x, upper = 0, 7
    bithelper = ''
    for bit in b:
        bithelper += str(int(bit))
        if x == upper:
            x = 0
            rList.append(int(bithelper, 2))
            bithelper = ''
        else:
            x += 1

    return rList


#logging.debug(xor2bins(key[0], binstring))

for item in listResults:
    resBytes = bintoByteArray(item)
    print(''.join([chr(byte) for byte in resBytes]))

def stringtobin(s):
    a = BitArray(hex=s)
    logging.debug(a.bin)
    return a.bin

#print(stringtobin('b'))
# val = stringtobin('256')
# print(str(val))
# testkey = '1001'
# x = 0

# for bit in str(val):

#    print(str(bit), str(x), str(testkey), str(int(bit) ^ int(testkey[x])))
#    if x == 3:
#        x = 0
#    else:
#        x += 1


