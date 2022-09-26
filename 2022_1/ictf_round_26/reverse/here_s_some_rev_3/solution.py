from Crypto.Util.number import long_to_bytes as l2b


delta = 0xa63554e3107ac1d1
power = 0x13371337
modulus = 2 ** 64


def reverse(f):
    return (f - delta) * pow(pow(0x1337, power, modulus), -1, modulus) % modulus


enc = [0x356E8E3ED82AF370, 0x4A1B896D4355DF6F, 0x690EED9626A0F11A, 0x0D940B10648ADD31A, 0x2E843A5DFDBB5438]
print("".join(map(lambda x: l2b(reverse(x))[::-1].decode(), enc)))
