a, b = tuple(map(int, input().split()))


def pow(a, b):
    result = 1
    for i in range(0, b):
        result *= a
    
    return result


print(pow(a, b))