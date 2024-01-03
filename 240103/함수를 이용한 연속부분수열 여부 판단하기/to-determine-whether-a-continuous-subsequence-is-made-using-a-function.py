n1, n2 = tuple(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))


def is_b(a, b):

    if n1 < n2:
        return False

    flag = False
    for i in range(n1):
        if a[i] == b[0]:
            for j in range(1, n2):
                if b[j] == a[i+j]:
                    flag = True
                else:
                    flag = False

        if flag:
            return True
    
        i += n2

    return False

if is_b(a, b):
    print("Yes")
else:
    print("No")