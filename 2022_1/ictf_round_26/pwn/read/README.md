# Read (125pts)

## Description

Yet another shellcoding challenge, only read(2) is allowed this time.

## Attachments

[file](./chall)

## Writeup

First read allows us to bypass the limit of shellcode. Then we need to find flag by trying reading chars to address (0x00000 - 0xFF000 with step 0x01000) (`read` returns number of bytes which were read if they were written to address)

After that we will use side-channel attack to recognize each byte of flag (using binary search, because we have 2 states: infinity loop and segfault)

[solution](./solution.py)

`ictf{leak_the_flag_with_side_channel}`
