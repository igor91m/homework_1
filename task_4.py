x = int(input("x = "))
mx = 0
while x > 0:
    c = x % 10
    if c >= mx: mx = c
    x //= 10
print(mx)