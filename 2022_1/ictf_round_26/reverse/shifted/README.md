# Shifted (50pts)

## Description

Oh no! The flag turned into a jumble of random characters! Good thing we have the script that encoded it... (also hi it's been a while since I've made a challenge)

## Attachments

[file](shifted.py)

## Writeup

Knowing, that flag has `ictf{...}` format, we can restore `mystery_num` (by subtracting first flag's char index and `i` char index) and than restore other steps of encrypting.

[solution](solution.py)

`ictf{sh1ft1ng_ch@rs_w1th_4_myst3ry_numb3r}`
