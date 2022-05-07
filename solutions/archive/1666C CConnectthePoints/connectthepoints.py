p = []
for _ in range(3):
    p.append(tuple(map(int, input().strip().split())))

xs, ys = [u[0] for u in p], [u[1] for u in p]
xs.sort()
ys.sort()

# find corner point
a, b, c = None, None, None
for i in range(3):
    x, y = p[i]
    if a is None and (x == xs[0] or x == xs[-1]) and (y == ys[0] or y == ys[-1]) and (x != xs[1] or y != ys[1]):
        a = p[i]
    elif b is None:
        b = p[i]
    else:
        c = p[i]

out = []

if c[0] == xs[1] and (b[0] != xs[1] or c[1] == ys[1]):
    b, c = c, b

if b[1] == ys[1]:
    out.append("3")
    out.append(" ".join(map(str, [a[0], a[1], b[0], a[1]])))
    out.append(" ".join(map(str, [b[0], a[1], b[0], c[1]])))
    out.append(" ".join(map(str, [b[0], c[1], c[0], c[1]])))
else:
    out.append("3")
    out.append(" ".join(map(str, [a[0], a[1], b[0], a[1]])))
    out.append(" ".join(map(str, [b[0], a[1], b[0], b[1]])))
    out.append(" ".join(map(str, [c[0], c[1], b[0], c[1]])))

print("\n".join(out))
