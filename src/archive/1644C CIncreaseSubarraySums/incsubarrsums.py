t = int(input().strip())

out = []
for _ in range(t):
    n, x = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))

    optimalSums = [0]
    sums = [0 for _ in range(n)]
    for c in range(n):
        optimal = None
        for i in range(n-c):
            s = sums[i] + a[i + c]
            sums[i] = s
            if optimal is None:
                optimal = s
            else:
                optimal = max(optimal, s)
        optimalSums.append(optimal)

    p = list(sorted(enumerate(optimalSums), key=lambda z: z[1], reverse=True))
    ans = []
    i = 0
    for k in range(n+1):
        if k > p[i][0]:
            for j in range(i+1, n+1):
                if p[j][1] + min(p[j][0], k) * x > p[i][1] + min(p[i][0], k) * x:
                    i = j
        ans.append(str(p[i][1] + min(p[i][0], k) * x))
    out.append(" ".join(ans))

print("\n".join(out))
