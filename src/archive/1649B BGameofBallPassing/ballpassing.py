t = int(input().strip())


out = []
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    a.sort(reverse=True)
    i, p = 1, a[0]
    while i < n and a[i] > 0:
        if a[i] >= p:
            p = 1
            break
        else:
            p -= a[i]
            i += 1
    out.append(str(p))

print("\n".join(out))
