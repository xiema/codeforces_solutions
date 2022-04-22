from sys import stdin, stdout
from bisect import bisect

t = int(stdin.readline().strip())

for _ in range(t):
    n,m = map(int, stdin.readline().split())
    ks = list(map(int, stdin.readline().split()))
    cs = list(map(int, stdin.readline().split()))

    cref = {}
    i = 1
    while i <= m:
        j = bisect(cs, cs[i - 1], i - 1)
        while i - 1 < j:
            cref[i] = j
            i += 1

    total = 0
    for i, k in enumerate(sorted(ks, reverse=True)):
        c = cref[k]
        if i < c - 1:
            total += cs[i]
        else:
            total += cs[c - 1]

    stdout.write(f"{total}\n")
