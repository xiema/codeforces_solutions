n = int(input().strip())
a = list(map(int, input().strip().split()))

def solve(a, i):
    acc, p = 0, 0
    for j in range(i-1, -1, -1):
        x = (p - 1) // a[j]
        acc += -x
        p = x * a[j]
    p = 0
    for j in range(i+1, n):
        x = (p + a[j]) // a[j]
        acc += x
        p = x * a[j]
    return acc

print(min(solve(a, i) for i in range(n)))
