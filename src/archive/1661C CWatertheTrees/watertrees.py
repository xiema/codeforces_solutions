from bisect import bisect

t = int(input().strip())

def solve(o, t):
    if t - o > 1:
        d = (t - o) // 3 + ((t - o) % 3 == 2)
        o, t = o + 2 * d, t - d
    return (o + (t > o)) * 2 - (o > t)


out = []
for _ in range(t):
    n = int(input().strip())
    h = list(map(int, input().strip().split()))
    mx = max(h)
    o, t, e = 0, 0, 0
    for x in h:
        e += (mx - x + 1) % 2
        o += (mx - x) % 2
        t += (mx - x) // 2
    out.append(str(min(solve(o, t), solve(e, t + o))))


print("\n".join(out))
