y = int(input())

def is_year(n):

    if n%4 ==0 and n%100==0 and n%400==0:
        return True

    if n%4 ==0 and n%100 == 0:
        return False

    if n%4 == 0:
        return True

    return False


if is_year(y):
    print("true")
else:
    print("false")