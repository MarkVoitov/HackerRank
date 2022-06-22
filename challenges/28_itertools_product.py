from itertools import product

a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

for i in product(a, b):
    print(i, end=' ')
