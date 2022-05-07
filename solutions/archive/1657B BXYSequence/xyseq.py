from math import sqrt

t = int(input().strip())

out = []
for _ in range(t):
    n, B, x, y = map(int, input().strip().split())
    ans, acc = 0, 0
    i = 0

    while i < n:
        d = B - acc
        if d >= x:
            m = min(n - i, d // x)
            ans += m * (acc + x + acc + m * x) // 2
            acc += m * x
            i += m
        else:
            m = min(n - i, -((d - x) // y))
            ans += m * (acc - y + acc - m * y) // 2
            acc -= m * y
            i += m
    out.append(str(ans))

print("\n".join(out))
