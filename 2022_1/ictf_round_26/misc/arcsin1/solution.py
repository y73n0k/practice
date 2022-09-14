from mpmath import mp
mp.dps = 100000
print("ictf{" + str(mp.pi)[10000:10000 + 100] + "}")
