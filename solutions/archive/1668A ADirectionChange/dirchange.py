t = int(input().strip())

for _ in range(t):
    n, m = map(int, input().strip().split())
    if (n == 1 and m > 2) or (m == 1 and n > 2):
        print(-1)
        continue
    a = max(n,m) - min(n,m)
    print((min(n,m) - 1) * 2 + (a // 2 * 4) + a % 2)
