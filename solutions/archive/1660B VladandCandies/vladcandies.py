t = int(input().strip())

def solve(n, a):
    if n == 1:
        return a[0] == 1
    a.sort(reverse=True)
    if a[0] - a[1] > 1:
        return False
    return True

for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    print("YES" if solve(n, a) else "NO")
