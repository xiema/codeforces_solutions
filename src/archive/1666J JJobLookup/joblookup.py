n = int(input().strip())

S = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j, c in enumerate(map(int, input().strip().split())):
        S[i][j] = c

for i in range(n):
    for j in range(n):
        if i > 0 and j > 0:
            S[i][j] += S[i][j-1] + S[i-1][j] - S[i-1][j-1]
        elif i > 0:
            S[i][j] += S[i-1][j]
        elif j > 0:
            S[i][j] += S[i][j-1]


def acc(i1, i2, j1, j2):
    if i1 >= i2 or j1 >= j2:
        return 0
    a = S[i2-1][j2-1]
    b = S[i2-1][j1-1] if j1 > 0 else 0
    c = S[i1-1][j2-1] if i1 > 0 else 0
    d = S[i1-1][j1-1] if i1 > 0 and j1 > 0 else 0
    return a - b - c + d

M = [[-1 for i in range(n)] for j in range(n)]
P = [[-1 for i in range(n)] for j in range(n)]
def solve(b, e):
    if e - b == 1:
        M[b][e-1] = 0
        return 0
    if e - b == 0:
        return 0
    if M[b][e-1] != -1:
        return M[b][e-1]
    M[b][e-1] = 1e18
    for i in range(b, e):
        s = solve(b, i) + solve(i+1, e)
        s += acc(0, b, b, i) + acc(b, i, i, n) + acc(0, i+1, i+1, e) + acc(i+1, e, e, n)
        if s < M[b][e-1]:
            M[b][e-1] = s
            P[b][e-1] = i
    return M[b][e-1]
solve(0, n)
sol = ["" for _ in range(n)]
def label(b, e, p):
    if e - b == 1:
        sol[b] = str(p)
        return
    elif e - b == 0:
        return
    i = P[b][e-1]
    sol[i] = str(p)
    label(b, i, i+1)
    label(i+1, e, i+1)
label(0, n, 0)
print(" ".join(sol))
