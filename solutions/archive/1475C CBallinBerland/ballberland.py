from sys import stdin, stdout

t = int(stdin.readline().strip())
for _ in range(t):
    _,_,k = map(int, stdin.readline().split())
    al = list(map(int, stdin.readline().split()))
    bl = list(map(int, stdin.readline().split()))
    ea, eb = {}, {}
    for a in al:
        ea[a] = ea.get(a, 0) + 1
    for b in bl:
        eb[b] = eb.get(b, 0) + 1
    c = 0
    for i in range(k):
        c += k - (ea[al[i]] + eb[bl[i]] - 1)
    stdout.write(f"{c//2}\n")
