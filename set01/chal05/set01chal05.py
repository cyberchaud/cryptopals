from pwn import *
import logging
from binascii import hexlify

logging.basicConfig(filename='set01chal05.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of challenge')

s1 = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
c1 = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272"
c2 = "a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

key = b"ICE"



def xorstr(s, k):
    ciphertext = ""
    logging.debug(s)
    logging.debug(k)
    ciphertext = xor(s, k)
    logging.debug(f'Returning {ciphertext}')
    return ciphertext

xortext = xorstr(s1, key)
logging.debug(f'Hexing the xor bytes: {xortext.hex()}')
print(xortext.hex())
