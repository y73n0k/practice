from string import printable

f = lambda c: "".join([chr([65279,8205,8204,8203][(c>>i)&3])for i in range(0,7,2)]).encode()

d = {f(ord(c)): c for c in printable}

flag = ""
with open("zeroed.py", "rb") as f:
    enc = f.read()
    enc = enc[1: enc.index(b"!")]
    for i in range(0, len(enc), 12):
        flag += d[enc[i: i+12]]
print(flag)
