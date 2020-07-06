# Cryptopals
# Set 01
# Challenge 01

# Convert hex to base64
# Tips - Always operate on raw bytes, never on encoded strings.  Only use hex and base64 for pretty-printing.

import base64
import logging
import binascii


def expectedResult(s):
    res = r'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    logging.debug('Result string is {}'.format(res))
    return (s == res)


def hextobase64(s):
    logging.debug("Inside hextoBase64")
    logging.debug("Value of s is: {}".format(s))
    return binascii.unhexlify(s)


def encodebase64(s):
    logging.debug("Inside encodeBase64")
    logging.debug("Value of s is: {}".format(s))
    return base64.b64encode(s).decode('ascii')


logging.basicConfig(filename='set01chal01.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of challenge')
Input = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
logging.debug('Input string is {}'.format(Input))
logging.debug('Converting string to base64')
rawString = hextobase64(Input)
logging.debug('Returned value is: {}'.format(rawString))

logging.debug('Encoding string to Base64')
b64String = encodebase64(rawString)
logging.debug('Returned value is: {}'.format(b64String))


logging.debug('Verifying result')
result = expectedResult(b64String)

print(result)

logging.debug('End of challenge')

