y, m, d = tuple(map(int, input().split()))


def is_leap():

    if y%4 != 0:
        return False
    
    if y%100 != 0:
        return True

    if y%400 != 0:
        return False

    return True


def is_exist(leap):

    if m == 2:
        if leap:
            return d <= 29
        else:
            return d <= 28

    if m == 4 or m == 6 or m == 9 or m == 11:
        return d <= 30
    
    else:
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


if is_leap():
    # 윤년 = 2월 28일까지
    if is_exist(True):
        print(seasons())
    else:
        print(-1)
    
else:
    if is_exist(False):
        print(seasons())
    else:
        print(-1)