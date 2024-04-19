n = int(input())
group = 2
while n % group != 0:
    group += 1
print(group)