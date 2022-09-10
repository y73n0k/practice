enc = "093d4f522f147c126a5d5a7f2162781a2f77225f1975734152133119741b0e333a620a6801561f1d6d673863650f78350463550d72713b24490c2e2f56092b59796b080c0f2460677b5f"
s = [int(enc[i: i + 2], 16) for i in range(0, len(enc), 2)]
length = len(s)
v4s = [0x0, 0x18, 0x2e, 0x19, 0x34, 0x1c, 0x36, 0x22, 0x2a, 0x11, 0x3a, 0x45, 0x2, 0x8, 0x48, 0x17, 0x4, 0x2a, 0x24, 0x37, 0x16, 0x6, 0x4, 0xc, 0x4, 0x4, 0x1c, 0x47, 0x2c, 0x2, 0x3c, 0x2b, 0x32, 0x14, 0x3c, 0x2c, 0x6, 0x0, 0x3a, 0x2d, 0xa, 0x24, 0xa, 0x1f, 0x4, 0x22, 0x2a, 0x2, 0x8, 0x46, 0xe, 0x13, 0x32, 0x46, 0x22, 0x13, 0x20, 0x30, 0x18, 0x22, 0xa, 0x42, 0x2c, 0x43, 0x10, 0x1e, 0x3a, 0x7, 0x3c, 0x3e, 0x6, 0x42, 0xc, 0x3e]
v5s = [0x2, 0x62, 0x17, 0x21, 0x32, 0x7c, 0x2e, 0x1a, 0x6b, 0x2b, 0x41, 0xd, 0x44, 0x56, 0x3a, 0x29, 0x1c, 0x78, 0x4c, 0x49, 0x65, 0x6a, 0x5b, 0x7e, 0x44, 0x56, 0x3a, 0x29, 0x1c, 0x78, 0x4c, 0x49, 0x65, 0x6a, 0x5b, 0x7e, 0x44, 0x56, 0x3a, 0x29, 0x1c, 0x78, 0x4c, 0x49, 0x65, 0x6a, 0x5b, 0x7e, 0x44, 0x56, 0x3a, 0x29, 0x1c, 0x78, 0x4c, 0x49, 0x65, 0x6a, 0x5b, 0x7e, 0x44, 0x56, 0x3a, 0x29, 0x1c, 0x78, 0x4c, 0x49, 0x65, 0x6a, 0x5b, 0x7e, 0x44, 0x56]

for i in range(length - 1, -1, -1):
    v4, v5 = v4s[i], v5s[i]
    s_i = s[i]
    s_v4 = s[v4]
    s[i] = s_v4 ^ v5
    s[v4] = s_i ^ v5
s[0] = ord("i")
print("".join(map(chr, s)))
