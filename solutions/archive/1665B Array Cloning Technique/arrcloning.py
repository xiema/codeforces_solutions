t = int(input().strip())

def count(a, x, b, e):
    if a[b] != x:
        return 0
    if b == e:
        return 1
    if a[e - 1] == x:
        return e - b
    m = (b + e) // 2
    return count(a, x, b, m) + count(a, x, m, e)

def solve(r, mc):
    if r == 0:
        return 0
    if mc >= r:
        return 1 + r
    if mc == 1:
        return 2 + solve(r - 1, 2)
    return 1 + mc + solve(r - mc, mc * 2)

for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))

    a.sort()
    mc = 0
    i = 0
    while i < n:
        c = count(a, a[i], i, n)
        if c > mc:
            mc = c
        i += c

    print(solve(n - mc, mc))
