n = int(input())
a = ''
b = True
while b:
    if n == 0:
        b = False
        break

    if n % 2 == 0:
        a += '*'
    else:
        n /= 2

print(a)