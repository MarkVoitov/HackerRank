from collections import defaultdict

n, m = list(map(int, input().split()))
d = defaultdict(list)

for i in range(1, n+1): d[input()].append(str(i))
for j in range(m): print(' '.join(d[input()]) or -1)
