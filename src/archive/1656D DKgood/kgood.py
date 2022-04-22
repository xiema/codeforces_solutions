t = int(input().strip())

out = []
for _ in range(t):
    n = int(input().strip())
    m = n & -n
    if n == m:
        out.append("-1")
    else:
        out.append(str(min(n // m, m * 2)))

print("\n".join(out))
