n = int(input())

def divid(a):
    result = 0

    for i in range(1, a+1):
        result += i
    
    return result//10


print(divid(n))