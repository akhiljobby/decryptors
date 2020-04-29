

#!/usr/bin/env python3
import argparse
import base64
import os
from xml.etree import ElementTree

from Crypto.Cipher import AES
from colorama import Fore, Style


def decrypt(cpass):
    
    padding = '=' * (4 - len(cpass) % 4)
    epass = cpass + padding
    decoded = base64.b64decode(epass)
    key = b'\x4e\x99\x06\xe8\xfc\xb6\x6c\xc9\xfa\xf4\x93\x10\x62\x0f\xfe\xe8' \
          b'\xf4\x96\xe8\x06\xcc\x05\x79\x90\x20\x9b\x09\xa4\x33\xb6\x6c\x1b'
    iv = '\x00' * 16
    aes = AES.new(key, AES.MODE_CBC, iv)
    result= aes.decrypt(decoded).decode(encoding='ascii').strip()
    print (result)
