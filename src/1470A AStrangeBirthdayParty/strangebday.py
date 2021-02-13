from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n,m = map(int, stdin.readline().split())
    ks = list(map(int, stdin.readline().split()))
    cs = list(map(int, stdin.readline().split()))
    cks = [cs[k-1] for k in ks]
    cks.sort()
    i, j = 0, 0
    total = sum(cks)
    memo = [total for _ in range(n)]
    for c in cs:
        _memo = []
        for i in range(n):
            s = total if i == 0 else memo[i-1]
            if c < cks[i]:
                s = s - cks[i] + c
            _memo.append(min(s, memo[i]))


    while i < n:
        while j < m and cs[j] > cks[i]:
            j += 1
        if j < m:
            s += cs[j]
            j += 1
        else:
            s += cks[i]
        i += 1
    stdout.write(f"{s}\n")
