t = int(input().strip())

def solve(n, c):
    o = False
    for i in range(n):
        if c[i] - c[(i-1)%n] > 1:
            return False
        if c[i] == 1:
            if not o:
                o = True
            else:
                return False
    return o

for _ in range(t):
    n = int(input().strip())
    c = list(map(int, input().strip().split()))
    print("YES" if solve(n,c) else "NO")
