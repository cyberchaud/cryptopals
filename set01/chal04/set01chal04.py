# Cryptopals
# Set 01
# Challenge 03

# Single-byte XOR cipher

# Used the pwn tools library to simplify

from pwn import *
from struct import *

logging.basicConfig(filename='set01chal04.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of challenge')

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

def sxor(s1, s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))

xorList = []
total = 0
highest = []
newhigh = []
hightotal = 0
freqtable = {'\ufeff': 1.3307605296426908e-05, 'p': 0.014052831193026815, 'r': 0.049344600439150975, 'o': 0.06342404684277064, 'j': 0.0023687537427639896, 'e': 0.09095748220107791, 'c': 0.020573557788276, 't': 0.0668174861933595, ' ': 0.1652405349657329, 'g': 0.016967196752944308, 'u': 0.022489852950961474, 'n': 0.04858606693725464, 'b': 0.011697385055559253, "'": 0.003473284982367423, 's': 0.04363563776698383, 'h': 0.04066804178588063, 'x': 0.000998070397232018, ',': 0.011018697185441479, 'y': 0.016421584935790805, 'l': 0.030314724865260496, 'a': 0.059285381595581874, 'm': 0.019349258101004723, 'k': 0.009874243129948767, 'i': 0.04871914299021891, 'f': 0.015902588329230156, '(': 0.00034599773770709963, '.': 0.01724665646416927, ')': 0.00034599773770709963, '\n': 0.02491183711491117, 'w': 0.019908177523454654, 'd': 0.037354448067070334, 'v': 0.005442810566238606, '-': 0.0038592055359638034, ':': 0.0008783019495641759, '2': 0.00022622929003925744, '0': 0.00026615210592853815, '8': 0.00013307605296426908, '[': 2.6615210592853816e-05, '#': 1.3307605296426908e-05, '4': 0.00021292168474283053, '3': 0.00022622929003925744, '9': 0.00021292168474283053, '7': 0.000146383658260696, ']': 2.6615210592853816e-05, '*': 0.001171069266085568, '/': 0.00041253576418923414, '1': 0.0007718411071927606, '5': 0.00017299886885354982, '_': 0.0007718411071927606, '!': 0.00027945971122496507, ';': 0.000572227027746357, '"': 0.009262093286313128, 'q': 0.0004657661853749418, '?': 0.0018098343203140595, 'z': 0.00017299886885354982, '6': 9.315323707498835e-05, '%': 1.3307605296426908e-05, '@': 2.6615210592853816e-05, '$': 2.6615210592853816e-05}

def Sort(list):
    logging.debug('Sorting new high freqs')
    list.sort(key = lambda x:[3])
    return list

with open("4.txt") as f:
    logging.debug('Opening the hexed lines')
    for line in f:
        line = bytes.fromhex(line)
        for byte in range(254):
            total = 0
            #xorList.append(xor(line, chr(byte)))
            xorLine = xor(line, chr(byte))
            for b in xorLine:
                total = freqtable.get(chr(b), 0) + total
            if total > hightotal:
                newhigh = []
                newhigh.append(chr(byte))
                newhigh.append(xorLine)
                newhigh.append(line)
                newhigh.append(total)
                highest.append(newhigh)
                hightotal = total
                if len(highest) >= 5:
                    Sort(highest)
                    highest = highest[-5:]
                    highest.append(newhigh)
                    logging.debug(highest)
    f.close()

logging.debug(xorList)

print(highest)