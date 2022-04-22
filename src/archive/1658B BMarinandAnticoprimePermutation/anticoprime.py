t = int(input().strip())

fact, acc = {}, 1
for i in range(1, 501):
    fact[i] = acc = (acc * i) % 998244353

ans = []
for _ in range(t):
    n = int(input().strip())
    if n % 2:
        ans.append("0")
    else:
        f = fact[n//2]
        ans.append(str((f * f) % 998244353))

print("\n".join(ans))
