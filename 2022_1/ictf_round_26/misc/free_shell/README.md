# Free Shell (100pts)

## Description

Here's your free shell, can you read the flag?

## Attachments

nc puzzler7.imaginaryctf.org 29466

## Writeup

Connecting, trying do `ls`. It is `Bad system call (core dumped)`.

Let's try bash builtins. They works, so we can list dir by `echo *` and read files via `echo "$(<file)"`

There is source of this shell

shell.c

```c
#include <seccomp.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <syscall.h>
#include <unistd.h>

void init(void) {
	scmp_filter_ctx filter = seccomp_init(SCMP_ACT_ALLOW);
	seccomp_rule_add(filter, 0, SYS_execve, 0);
	seccomp_load(filter);
}

int main() {
	init();
	syscall(SYS_execveat, 0, "/bin/bash", 0, 0, 0);  // free shell!!!
	return 0;
}
```

Any execve syscalls are killed, that's why we can't run commands (because of `fork` + `execve` syscalls)

We need to find some way to use `execveat` syscall to execute /readflag. We can dynamically load a custom loadable bash builtins with `enable -f`.

Solutions:

[source_of_builtin.c](./zxc.c)

[compiled_builtin](./zxc)

[solution.py](./solution.py)

`ictf{I_hope_you_didn't_pwn_bash}`
