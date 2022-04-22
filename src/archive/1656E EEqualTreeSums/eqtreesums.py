from sys import stdin, stdout
t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    T = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, stdin.readline().strip().split())
        T[u-1].append(v-1)
        T[v-1].append(u-1)

    q = [(0, 0)]
    A = [0] * n
    S = [False] * n
    A[0] = -1

    while q:
        u, p = q.pop()
        S[u] = True
        A[u] += -(p % 2) * 2 + 1
        for v in T[u]:
            if not S[v]:
                q.append((v, p + 1))
                A[u] += -(p % 2) * 2 + 1

    stdout.write(" ".join(map(str, A)) + "\n")
