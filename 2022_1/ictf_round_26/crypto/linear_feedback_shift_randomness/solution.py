from hashlib import sha256


def H(m):
    return int.from_bytes(sha256(m).digest(), 'big')


FALG = ...
HASHES = list(map(lambda x: H(x.encode()), FLAGS))


sigs = ...
p = 155539674196487197654234954630895243597382433050914816320012284042611125173503
y = 96840893270506615428903134623877213335468697861345751428505976799297422928446
q = (p - 1) // 2

taps = [0, 7, 36, 57, 95, 104, 127]
indices = [1, 8, 37, 58, 96, 105, 128]
a = pow(sigs[129][1], -1, q) * HASHES[129 % 39] % q
for ind in indices:
    a = (a - pow(sigs[ind][1], -1, q) * HASHES[ind % 39]) % q
b = -(pow(sigs[129][1], -1, q) * sigs[129][0])
for ind in indices:
    b += pow(sigs[ind][1], -1, q) * sigs[ind][0]
x = a * pow(b, -1, q) % q
assert pow(2, x, p) == y

def K(s, h, x, r, q):
    return pow(s, -1, q) * (h + x * r) % q
k0 = K(sigs[128 - 1][1], HASHES[128 % 39 - 1], x, sigs[128 - 1][0], q)
for ind in taps[1:]:
    k0 = (k0 - K(sigs[ind - 1][1], HASHES[ind % 39 - 1], x, sigs[ind - 1][0], q)) % q


from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

enc = bytes.fromhex(...)
key = k0.to_bytes(32, 'big')
aes = AES.new(key[:16], AES.MODE_CBC, key[16:])
print(unpad(aes.decrypt(enc), 16).decode())
