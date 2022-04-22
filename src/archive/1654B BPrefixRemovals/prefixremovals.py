t = int(input().strip())

out = []
for _ in range(t):
    s = input().strip()
    i, n = 0, len(s)
    while i < n - 1:
        for j in range(i+1, n):
            if s[i] == s[j]:
                i += 1
                break
        else:
            break
    out.append(s[i:])

print("\n".join(out))
