from sys import stdin, stdout

def solve(n, d):
    dm =  {}
    for v in d:
        dm[v] = dm.get(v, 0) + 1
    ds = sorted(list(dm.items()))
    if len(ds) != n or ds[-1][0]%(n*2) != 0:
        return False
    prev, s, i = None, 0, 0
    for x, c in ds:
        if x%2 != 0 or c != 2:
            return False
        if i != 0:
            if (x - prev)%(i*2) != 0:
                return False
            s += (x - prev)//i
        prev = x
        i += 1
    if s * n >= ds[-1][0]:
        return False
    return True



t = int(stdin.readline().strip())
for _ in range(t):
    n = int(stdin.readline().strip())
    d = list(map(int, stdin.readline().split()))
    if solve(n,d):
        stdout.write("YES\n")
    else:
        stdout.write("NO\n")
