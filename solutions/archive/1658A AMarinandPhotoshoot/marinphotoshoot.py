t = int(input().strip())

out = []
for _ in range(t):
    n = int(input().strip())
    s = input().strip()
    ans, req = 0, 0
    for i, c in enumerate(s):
        if c == "0":
            if req > 0:
                ans += req
            req = 2
        else:
            req = max(0, req - 1)
    out.append(str(ans))

print("\n".join(out))
