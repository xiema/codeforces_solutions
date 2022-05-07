t = int(input().strip())

for _ in range(t):
    a, b = map(int, input().strip().split())
    if a > 0:
        c = b * 2 + a + 1
    else:
        c = 1
    print(c)
