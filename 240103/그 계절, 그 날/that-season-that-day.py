y, m, d = tuple(map(int, input().split()))


def is_leap():

    if y%4 != 0:
        return False
    
    if y%100 != 0:
        return True

    if y%400 != 0:
        return False

    return True


def is_exist():

    if m == 2:
        return d <= 29 if is_leap() else d <= 28

    if m == 4 or m == 6 or m == 9 or m == 11:
        return d <= 30
    
    return d <= 31


def seasons():
    if m == 3 or m == 4 or m == 5:
        return "Spring"
    elif m == 6 or m == 7 or m == 8:
        return "Summer"
    elif m == 9 or m == 10 or m == 11:
        return "Fall"
    else:
        return "Winter"


if is_exist():
    print(seasons())
else:
    print(-1)