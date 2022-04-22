t = int(input().strip())

def solve2(n, c, a):
    m = [0] * (c+1)
    cnt = [0] * (c+1)

    for x in a:
        cnt[x] += 1

    for i in range(1, c+1):
        m[i] = m[i-1] + cnt[i]

    for x in sorted(list(set(a))):
        i = 1
        while i * x <= c:
            mn = i * x - 1
            mx = min(c, (i + 1) * x - 1)
            if m[mx] - m[mn] > 0 and cnt[i] == 0:
                return False
            i += 1

    return True



out = []
for _ in range(t):
    n, c = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))

    out.append("Yes" if solve2(n, c, a) else "No")

print("\n".join(out))
