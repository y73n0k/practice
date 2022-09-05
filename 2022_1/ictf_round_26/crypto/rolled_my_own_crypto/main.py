from Crypto.Util.number import getPrime, isPrime, inverse
from hashlib import sha256
from random import randrange

q, g = 0, 2
while not isPrime(p := 2*q + 1) or pow(g, q, p) != 1:
    q = getPrime(256)

x = randrange(2, q)
y = pow(g, x, p)

def H(m):
    return int.from_bytes(sha256(m).digest(), 'big')

def sign(m):
    k = randrange(2, q)
    r = pow(g, k, p) % q
    s = (H(m) + r*x) * inverse(k, q) % q
    return r, s

def verify(m, r, s):
    u = inverse(s, q)
    return pow(g, u * H(m), p) * pow(y, u * r, p) % p % q == r

def main():
    print("Hello admin, here are the parameters!")
    print('p =', p)
    print('y =', y)

    print("Please sign a message to retrieve your flag:")
    m = bytes.fromhex(input('m = '))
    r = int(input('r = '))
    s = int(input('s = '))

    if not verify(m, r, s):
        print("I've called the cops!")
        exit()

    if m != b"I'm the admin and I'd like to get my flag.":
        print("Who are you??")
        exit()

    print("Verification successful! Here is your flag: ", end='')
    with open('flag.txt', 'r') as file:
        print(file.read(), flush=True)

if __name__ == '__main__':
    main()