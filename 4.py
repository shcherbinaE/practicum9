a = int(input())
c = 0
while a != 0:
    if a % 4 == 0:
        c += 1
    a = int(input())
print(c)