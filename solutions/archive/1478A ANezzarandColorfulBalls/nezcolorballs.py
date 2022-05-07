from sys import stdin

t = int(stdin.readline().strip())
for _ in range(t):
    n = int(stdin.readline().strip())
    a = list(map(int, stdin.readline().split()))
    m = 1
    i, j = 0, 1
    while j < n:
        if a[i] != a[j]:
            m = max(m, j-i)
            i = j
        j += 1
    else:
        m = max(m, j-i)
    print(m)
