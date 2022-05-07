from sys import stdin, stdout
from bisect import bisect

n, C = map(int, stdin.readline().strip().split())
U = []
for i in range(n):
    c, d, h = map(int, stdin.readline().strip().split())
    U.append((c, -d*h, d, h))
U.sort()
A = [-1 for _ in range(1000001)]
for c, dhn, d, h in U:
    acc, x = c, -dhn
    if acc <= C and x <= A[acc]:
        continue
    while acc <= C:
        A[acc] = max(A[acc], x)
        acc, x = acc + c, x - dhn
cur = -1
for i in range(1, C+1):
    A[i] = cur = max(A[i], cur)

m = int(input().strip())
for j in range(m):
    D, H = map(int, stdin.readline().strip().split())
    i = bisect(A, D * H, 0, C+1)
    if i > C:
        i = -1
    stdout.write(f"{i} ")
