n = input()

def is_satisfied(n):
    m = int(n)
    if m%2 == 0:
        if (int(n[:1]) + int(n[1:]))%5 == 0:
            return True
    
    return False


if is_satisfied(n):
    print("Yes")
else:
    print("No")