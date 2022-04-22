from sys import stdin, stdout

t = int(stdin.readline().strip())

out = []
for _ in range(t):
    stdin.readline()
    n, m = map(int, stdin.readline().strip().split())
    n2 = n * 2
    pts, weight = [None] * m, 0
    for i in range(m):
        x, w = map(int, stdin.readline().strip().split())
        pts[i] = (w, x, i)
    pts.sort(key=lambda z: z[0])
    segs = [None] * n2
    i = 0
    for p in pts:
        weight += p[0]
        segs[i] = p
        i += 1
        if i == n2:
            break
    segs.sort(key=lambda z: z[1])
    stdout.write(f"{str(weight)}\n")
    for i in range(n):
        stdout.write(f"{segs[i][2] + 1} {segs[-i-1][2] + 1}\n")
    stdout.write("\n")
