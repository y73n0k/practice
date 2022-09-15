# Box (50pts)

## Description

`ciphertext=magic(flag)(flag)`

## Attachments

[file](./challenge.py)

## Writeup

Expanding expression brackets, we can conclude that `box` is just `f(x) = a * x + b`

So, knowing 2 variables and 2 results of functions, we can get `a` and `b`, and then recover flag.

[solution](./solution.py)

`ictf{wow_such_linear_so_easy`
