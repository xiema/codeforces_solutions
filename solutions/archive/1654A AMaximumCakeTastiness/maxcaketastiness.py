t = int(input().strip())

out = []
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    a.sort(reverse=True)
    out.append(str(a[0] + a[1]))

print("\n".join(out))
