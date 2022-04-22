t = int(input().strip())

sol = []
a = 1
while a < 1e9:
    sol.append(str(a))
    a *= 3

out = []
for _ in range(t):
    n = int(input().strip())
    if n <= len(sol):
        out.append("YES")
        out.append(" ".join(sol[:n]))
    else:
        out.append("NO")

print("\n".join(out))
