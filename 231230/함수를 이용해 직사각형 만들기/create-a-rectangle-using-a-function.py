def rectangle(n, m):
    for _ in range(n):
        print("1" * m)


row, col = tuple(map(int, input().split()))
rectangle(row, col)