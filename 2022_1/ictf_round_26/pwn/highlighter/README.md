# Highlighter (50pts)

## Description

Writing is also important.

## Attachments

[file](vuln)

## Writeup

We can write anything to writable section, so overwrite `memset@GOT` with `puts@PTL` to print flag.

Solution:

[solution.py](./solution.py)

`ictf{writing_is_hard_but_satisfying_sometimes}`
