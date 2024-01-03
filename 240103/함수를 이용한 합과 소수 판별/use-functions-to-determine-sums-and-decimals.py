a, b = tuple(map(int, input().split()))


def is_satisfied(n):
    sum = 0

    if n == 1:
        return False
    
    for i in range(2, n):
        if n%i == 0:
            return False
        
    while n > 0:
        sum += n%10
        n //= 10
        
    if sum%2 == 0:
        return True
    
    return False


cnt = 0
for i in range(a, b+1):
    if is_satisfied(i):
        cnt += 1

print(cnt)