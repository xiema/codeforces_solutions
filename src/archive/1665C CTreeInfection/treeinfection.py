from bisect import bisect, bisect_left

t = int(input().strip())

out = []
for _ in range(t):
    n = int(input().strip())
    T = {0: [1], 1: []}
    i = 2
    for p in map(int, input().strip().split()):
        T.setdefault(p, []).append(i)
        i += 1
    c = [len(T[k]) for k in T]
    c.sort()

    U = {}
    for i, x in enumerate(c):
        u = x - i - 1
        if u > 0:
            U[u] = U.get(u, 0) + 1

    D = list(U.items())
    D.sort(reverse=True)
    i, l, y, z = 0, len(D), 0, 0
    while i < l:
        x, d = D[i]
        z += d
        if i == l - 1:
            y += (x - y) * z // (z + 1) + (((x - y) * z) % (z + 1) != 0)
            break
        else:
            a = (x - y) * z // (z + 1) + (((x - y) * z) % (z + 1) != 0)
            b = (x - D[i+1][0]) * z
            if b < a:
                y += b
                i += 1
            else:
                y += a
                break

    out.append(str(y + len(c)))

print("\n".join(out))
