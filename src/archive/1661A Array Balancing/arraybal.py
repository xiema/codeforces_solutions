t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))

    s = 0

    for i in range(0, n - 1):
        j = i + 1
        s1 = abs(a[i] - a[j]) + abs(b[i] - b[j])
        s2 = abs(a[i] - b[j]) + abs(b[i] - a[j])
        s += min(s1, s2)

    print(s)
