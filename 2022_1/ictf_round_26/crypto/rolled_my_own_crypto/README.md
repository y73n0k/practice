# Rolled my own Crypto (90pts)

## Description

DSA is so easy to implement! Why do people tell me I shouldn't roll my own crypto?

## Attachments

[file](main.py)

## Writeup

Vulnerable function is `verify`. We control `r` and `s`, so `u` as well.

We can rewrite last expression of function as

`pow((pow(g, H(m)) * pow(y, r)), u) % p % q == r`

Let `r = 1`, so we get `pow((pow(g, H(m)) * y), u) % p % q == 1`

So we need `u = 0`

Function `inverse` returns `0`, when inverse integer doesn't exist.

In case `q` is prime, we can pass `0` as parameter or integer which divided by `q`

Sum up:

```
m = 49276d207468652061646d696e20616e6420492764206c696b6520746f20676574206d7920666c61672e
r = 1
s = 0
```

`ictf{TH15_I5_TH3_R34S0N}`
