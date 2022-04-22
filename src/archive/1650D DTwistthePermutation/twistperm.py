t = int(input().strip())

def solve(n, a):
    pos = {}
    for i, x in enumerate(a):
        pos[x] = i

    lim = n
    l = []
    for i in range(n, 0, -1):
        d = (pos[i] + 1) % i
        l.append(d)
        for j in range(1, i):
            pos[j] = (pos[j] - d) % i
    return reversed(l)


for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    print(" ".join(str(i) for i in solve(n, a)))
