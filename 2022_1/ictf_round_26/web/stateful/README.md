# Stateful (100pts)

## Description

Time to build a lottery.

## Attachments

<https://stateful:re1eNaivee@stateful.031337.xyz>

## Writeup

Source code of backend:

```python
import flask
import pygments, pygments.lexers, pygments.formatters, pygments.lexers, nord_pygments
import os, json, hashlib, random
from Crypto.Cipher import AES

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "flag.txt")) as f:
    FLAG = f.read().strip()

app = flask.Flask(__name__)
app.secret_key = os.urandom(32)

def load_session():
    if 'x' not in flask.session:
        return {}
    cipher = AES.new(hashlib.sha256(app.secret_key).digest(), AES.MODE_ECB)
    return json.loads(cipher.encrypt(flask.session['x']))

def store_session(ses):
    d = json.dumps(ses).encode()
    while len(d) % 16 != 0: d += b" "
    cipher = AES.new(hashlib.sha256(app.secret_key).digest(), AES.MODE_ECB)
    flask.session['x'] = cipher.decrypt(d)

@app.route("/play/<int:guess>")
def play(guess: int):
    if not (ses := load_session()):
        return flask.redirect("/start")
    seed = bytes.fromhex(ses['seed'])
    rnd = random.Random(seed)
    for _ in range(ses['correct'] + 1):
        target = rnd.randint(13, 37)
    if guess == target:
        ses['correct'] += 1
    else:
        ses['correct'] = 0
    store_session(ses)
    return flask.redirect("/status")

@app.route("/status")
def status():
    ses = load_session()
    if not ses:
        return "The only winning move is not to play... Smart!"
    to_go = 42 - ses['correct']
    if to_go:
        return f"You're getting there, only {to_go} victories left; here's a hint: {ses['seed'][:4]}"
    return f"You broke the bank and now we're out of business. I hope you're happy with yourself. {FLAG}"

@app.route("/start")
def start():
    seed = os.urandom(32)
    store_session({"correct": 0, "seed": seed.hex()})
    return flask.redirect("/status")

@app.route("/")
def serve():
    content = open(__file__).read()
    try:
        lexer = pygments.lexers.get_lexer_for_filename(__file__)
    except:
        lexer = pygments.lexers.special.TextLexer()
    nord_pygments.Nord.background_color = "#2e3440"
    return pygments.highlight(content, lexer, pygments.formatters.HtmlFormatter(full=True, style=nord_pygments.Nord))


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
```

We see that value `correct` stores in cookie, so we can just store cookie with row of correct answers and take guess without loosing progress.

[solution](./solution.py)

`ictf{c0uld_w3_d0_some_k1nd_of_SGX_s34l1ng?}`
