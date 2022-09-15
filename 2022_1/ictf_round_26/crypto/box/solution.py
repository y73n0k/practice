from Crypto.Util.number import long_to_bytes

x1, y1 = 1337, 3011454617406654839679120250
x2, y2 = 0x1337, 10002638090931457241529120250

a = (y2 - y1) // (x2 - x1)
b = y2 - a * x2
print(f"Box is: f(x) = {a} * x + {b}")
y_flag = 5545457088879574964209613711409478327714366805681091501255101702161458272094830554232779120250
x_flag = (y_flag - b) // a
print(long_to_bytes(x_flag).decode())
