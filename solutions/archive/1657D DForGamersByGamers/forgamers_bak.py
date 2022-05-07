from sys import stdout
from bisect import bisect_left

n, C = map(int, input().strip().split())
U = []
for i in range(n):
    c, d, h = map(int, input().strip().split())
    U.append((d * h / c, c, d, h))
U.sort()
I = [u[0] for u in U]

m = int(input().strip())
for j in range(m):
    D, H = map(int, input().strip().split())
    i = bisect_left(I, D * H // C)
    x, mn = n, C + 1
    while i < n:
        if C // U[i][1] * U[i][2] * U[i][3] > D * H:
            s = (D * H + (U[i][2] * U[i][3])) // (U[i][2] * U[i][3]) * U[i][1]
            if s < mn:
                x, mn = i, s
        i += 1
    if x < n:
        stdout.write(f"{mn} ")
    else:
        stdout.write("-1 ")
