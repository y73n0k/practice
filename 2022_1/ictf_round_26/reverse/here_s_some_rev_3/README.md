# Here's some Rev v3 (75pts)

## Description

Yet another lazy reverse challenge because there is no other challenge today.

## Attachments

[file](./chall)

## Writeup

Each 8 bytes of flag are used as a seed of a LCG and loop for `0x13371337` times. So we can represent the result as 

`res = a^n * x + b (mod 2^64)`

`a`, `n` are given, we can get `b` by running loop with init value = `0`

[get_coef](./solution.c)

And we get `x = (res - b) * (a^n)^-1 (mod 2^64)`

[solution](./solution.py)

`ictf{sorry_for_today's_boring_challenge}`
