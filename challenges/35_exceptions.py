t = int(input())

for i in range(t):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except (ZeroDivisionError, ValueError) as e:
        print('Error Code:', e)
