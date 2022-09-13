from string import printable

enc = bytes(bytearray.fromhex("a9af6782b63c6cc8dcd29411e1463d3c46d6df794e7372187a47cf8b1d42167a85187f9eeb6567afda5d42d9c724c2cee7a5e2e6392f2b5c3e066f46990fc9063fa73ba8aad49bd7a0"))

def H(flag):
    return bytes([pow(x ^ hash(tuple(flag[:i])), 21127266505527, 251) & 255 for i, x in enumerate(flag)])

flag = b"ictf{"

while len(flag) != len(enc):
    for c in printable:
        if enc.startswith(H(flag + bytes([ord(c)]))):
            flag += bytes([ord(c)])
            break
print(flag.decode())
