n1, n2 = tuple(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))


def is_b(a, b):
    for i in range(n1):
        if a[i] == b[0]:
            for j in range(n2):
                if b[j] != a[i+j]:
                    return False
                return True
    
    return False


if is_b(a, b):
    print("Yes")
else:
    print("No")