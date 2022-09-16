# po4jie3mi4ma3 (75pts)

## Description

I managed to leak a database and some of the source code of this Chinese website. However, I'm having a lot of trouble actually getting into the site. I've recreated the relevant bits, maybe you'll have more luck?

## Attachments

puzzler7.imaginaryctf.org:5003

## Writeup

Site backend source:

```python
#!/usr/bin/env python3

from flask import Flask, Response, request

from hashlib import sha512
from pinyin import get # pip install pinyin

app = Flask(__name__)

db = {}

def make_user(username):
    default_pass = open("pass.txt").read().strip()
    assert len(default_pass) == 2
    text = get(default_pass, format="numerical").encode()
    db[username] = sha512(b'ictf{'+text+b'}').hexdigest()

@app.route('/')
def index():
    return Response(open(__file__).read(), mimetype='text/plain')

@app.route('/leak_db')
def leak():
    return Response(str(db), mimetype='text/plain')

@app.route('/login', methods=["GET"])
def login_get():
    return '''
    <h1>Login</h1>
    <br><br>
    <form action="/login" method="post">
        Username: <textarea name="user" id='user' rows="1" cols="75"></textarea><br>
        Password: <textarea name="pass" id='pass' rows="1" cols="75"></textarea><br>
        <input type="submit" value="Login"></input>
    </form>
    '''

@app.route('/login', methods=["POST"])
def login_post():
    user = request.form['user']
    pwd = request.form['pass']
    if db[user] == sha512(pwd.encode()).hexdigest():
        return f"Logged in successfully as {user}"
    else:
        return "Invalid credentials!"


if __name__ == '__main__':
    make_user('admin')
    app.run("0.0.0.0", 5003)
```

`pinyin`: Translate chinese chars to pinyin based on Mandarin.dat

So let's brute 2 chinese chars:

[solution](./solution.py)

`ictf{mu4ma3}`
