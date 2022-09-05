import string


new_alphabet = list(string.ascii_lowercase + string.digits + string.punctuation)
enc_flag = """15[=>ts-!]kgjhz%6cn~";=;.1b3:>}sq7n'\^]42t"""
# flag is ictf{...}
mystery_num = new_alphabet.index(enc_flag[0]) - new_alphabet.index("i")  # restore mystery_num

def shift(char):
    index = new_alphabet.index(char)
    new_index = (index - mystery_num) % len(new_alphabet)
    return new_alphabet[new_index]

flag = ""
for char in enc_flag:
    flag += shift(char)
    mystery_num += 10
print(flag)