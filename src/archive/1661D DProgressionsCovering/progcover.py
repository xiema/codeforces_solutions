n, k = map(int, input().strip().split())
b = list(map(int, input().strip().split()))

acc, m, q, s, j = 0, 0, [], 0, 0
for i in range(n-1, -1, -1):
    acc -= s
    if j < len(q) and i == q[j][0]:
        s -= q[j][1]
        j += 1
    d = b[i] - acc
    if d > 0:
        l = k if i > k - 1 else i + 1
        x = (d + l - 1) // l
        if i > k - 1:
            q.append((i - k, x))
        m += x
        s += x
        acc += x * l

print(m)
