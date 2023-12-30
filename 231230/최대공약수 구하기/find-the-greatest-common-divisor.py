n, m = tuple(map(int, input().split()))

def gcd(a, b):
    n = a%b
    while(n != 0):
        a = b
        b = n
        n = a%b
    
    print(b)


gcd(n, m)