n, m = tuple(map(int, input().split()))

def lcm(a, b):
    for i in range(max(a, b), a*b):
        if (i%a == 0 and i%b == 0):
            return i

    return a*b

print(lcm(n, m))