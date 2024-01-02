a, b = tuple(map(int, input().split()))

def is_satisfied(n):
    check = str(n)
    return (check.find('3') != -1) or (check.find('6') != -1) or (check.find('9') != -1) or (n%3 == 0)


count = 0
for i in range(a, b+1):
    if is_satisfied(i):
        count += 1

print(count)