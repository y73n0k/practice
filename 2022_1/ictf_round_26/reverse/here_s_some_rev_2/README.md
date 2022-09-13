# Here's some Rev v2 (75pts)

## Description

Just another lazy reverse challenge because there is no other challenge today.

## Attachments

[file1](./chall.pyc)
[file2](./output.txt)

## Writeup

Use `decompyle3` to get source code:

```python
flag = open('flag.txt', 'rb').read().strip()

def H(flag):
    return bytes([pow(x ^ hash(tuple(flag[:i])), 21127266505527, 251) & 255 for i, x in enumerate(flag)])


enc = H(flag)
print(enc.hex())
```

Each byte of flag depends on previous, so we will brute each char of flag:

[solution](./solution.py)

`ictf{this_challenge_is_created_because_there_is_no_other_challenge_today}`
