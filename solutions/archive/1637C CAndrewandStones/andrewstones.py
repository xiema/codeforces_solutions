t = int(input().strip())

def solve(n, a):
    b1, b2 = False, False
    ops = 0
    for i in range(1, n-1):
        if a[i] != 1:
            b1 = True
        if i > 1 or a[i] % 2 == 0:
            b2 = True
        ops += (a[i] + a[i] % 2) // 2
    return ops if b1 and b2 else -1

out = []
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    out.append(str(solve(n, a)))

print("\n".join(out))
