# Hacking 101 (75pts)

## Description

Class is now in session. Today's homework is to figure out the answer to the homework. I hope you were taking notes...

## Attachments

Join https://www.gradescope.com/ with the class code 57DJPX as a student of Duke University. You will need a valid email, but it doesn't have to be a student email.

Please make a file `flag_printer.py` that prints the flag when run to pass the assignment.

## Writeup

After registration, we get access to task. This site run python script, so, firstly, I tried to make request on my server through script. It worked, then I just call `Popen`, get output and send it to my server. (After flag submission I found out that `pty` is part of python's stdlib, so I could just make a reverse shell)

[flag_printer.py](./flag_printer.py)

`ictf{you_have_been_expelled_for_academic_dishonesty}`
