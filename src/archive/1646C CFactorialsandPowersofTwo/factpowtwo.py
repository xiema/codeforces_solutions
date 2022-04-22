from itertools import combinations

t = int(input().strip())

fact = []
p, i = 6, 3
while p < 1e12:
    fact.append(p)
    i += 1
    p *= i

fc = {}
for i in range(1, len(fact) + 1):
    fc[i] = []
    for c in combinations(fact, i):
        fc[i].append(sum(c))


def count(x):
    c = 0
    while x > 0:
        c += x % 2
        x = x >> 1
    return c

out = []
for _ in range(t):
    n = int(input().strip())
    mn = count(n)
    for i, vals in fc.items():
        for v in vals:
            if v <= n:
                mn = min(mn, count(n - v) + i)
    out.append(str(mn))

print("\n".join(out))
