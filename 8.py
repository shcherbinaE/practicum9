x = int(input())
c = 0
for i in range(1, int(x ** 0.5) + 1):
    for j in range(i + 1, int(x ** 0.5) + 1):
        if i ** 2 + j ** 2 == x:
            c += 1
print(c)