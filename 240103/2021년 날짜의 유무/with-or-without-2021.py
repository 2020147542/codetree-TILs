m, d = tuple(map(int, input().split()))

def is_exist():
    if m > 13:
        return False
    
    odd = [1, 3, 5, 7, 8, 10, 12]
    if m in odd:
        if d > 32:
            return False
        
    elif m == 2:
        if d > 29:
            return False

    else:
        if d > 31:
            return False
    
    return True


if is_exist():
    print("Yes")
else:
    print("No")