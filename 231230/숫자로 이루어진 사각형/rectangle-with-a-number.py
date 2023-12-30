def square(n):
    result = []
    i = 0

    for _ in range(n):
        for _ in range(n):
            i = (i+1)%10 if i != 9 else 1
            print(i, end = " ")
        
        print()


num = int(input())
square(num)