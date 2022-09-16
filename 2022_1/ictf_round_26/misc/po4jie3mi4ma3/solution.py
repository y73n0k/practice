from hashlib import sha512
from pinyin import get

hash = 'bcfae3f2e987121fb0b7527511d99a7ef4ef3213e1c2993b0016758990f5c01fd109ba819e879f8d6cff2bd79e61a7ef62a8beb7eb8fb655ce3b22a63fec1cd0'

for a in range(0x4e00, 0x9fff + 1):
    for b in range(0x4e00, 0x9fff + 1):
        flag = b'ictf{' + get(chr(a) + chr(b), format="numerical").encode() + b'}'
        if sha512(flag).hexdigest() == hash:
            print(flag.decode())
            exit()
