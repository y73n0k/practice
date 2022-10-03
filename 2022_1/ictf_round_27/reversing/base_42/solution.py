from Crypto.Util.number import long_to_bytes as l2b


alphabet = "0123456789aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpP"
enc = "0koA439lJklKBLkABeK3oikB1GL1lelO0lCp50Kii0LFEbcdm1Il17GNKCj6P5KB0mpAfe4pAJ0p5lHb0kIC7K0I03meMpIG"
enc = [enc[i: i + 32] for i in range(0, len(enc), 32)]


flag = ""
for i in range(3):
    long = 0
    for c in enc[i]:
        long *= len(alphabet)
        long += alphabet.index(c)
    flag += l2b(long).decode()

print(flag)
