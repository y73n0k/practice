# Highlights (50pts)

## Description

Reading is important.

## Attachments

[file](highlights)

## Writeup

`checksec` result:
```
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```

`PIE` is enabled => all local variables will have same address in each program run.

Opening `main` function, see that flag stores in local variable `flag`. It starts `0x404080` and ends `0x404100`, so we will loop over all addresses and get flag.

[solution](solution.py)

`ictf{only_skill_more_important_than_reading_is_googling}`
