t = int(input().strip())

for _ in range(t):
    n, m = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    a.sort(reverse=True)
    s = a[0] + n
    for i in range(n - 1):
        s += a[i]

    if s <= m:
        print("YES")
    else:
        print("NO")
