a, b = tuple(map(int, input().split()))
result = 0


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True


for i in range(a, b+1):
    if is_prime(i):
        result += i

print(result)