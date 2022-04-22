t = int(input().strip())

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0

def repl(q, x, c, i):
    q[i][0], q[i][1] = x, c
    if q[2]:
        q[1-i][0], q[1-i][1] = x, c
def solve(t, q, x, b):
    i = 0 if b else 1

    if q[i][0] > 0:
        if q[i][0] + x > 0:
            repl(q, q[i][0] + x, 1, i)
            t += 1
        elif q[i][0] + x < 0:
            repl(q, q[i][0] + x, 1, i)
            t -= 1
        else:
            repl(q, 0, 2, i)
            t -= 1
    elif q[i][0] < 0:
        if q[i][0] + x > 0:
            repl(q, q[i][0] + x, 1, i)
            t += 3
        elif q[i][0] + x < 0:
            repl(q, x, 1, i)
            q[2] = False
            if x > 0:
                t += 1
            elif x < 0:
                t -= 1
        else:
            repl(q, 0, 2, i)
            t += 1
    else:
        if x > 0:
            t += q[i][1] + 1
            repl(q, x, 1, i)
        elif x < 0:
            repl(q, x, 1, i)
            q[2] = False
            t -= 1
        else:
            repl(q, x, q[i][1] + 1, i)

    return t, q

def copy(a, b):
    b[0][0], b[0][1] = a[0][0], a[0][1]
    b[1][0], b[1][1] = a[1][0], a[1][1]
    b[2] = a[2]

out = []
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    memo = [[sign(i), [[i, 1], [i, 1], True], [[i, 1], [i, 1], True]] for i in a]

    for k in range(1, n):
        for i in range(n - k):
            t1, q1 = solve(memo[i][0], memo[i][2], a[i+k], False)
            t2, q2 = solve(memo[i+1][0], memo[i+1][1], a[i], True)
            if t1 > t2:
                memo[i][0] = t1
                copy(q1, memo[i][1])
            elif t2 > t1:
                memo[i][0] = t2
                copy(q2, memo[i][1])
                copy(q2, memo[i][2])
            else:
                memo[i][0] = t1
                copy(q2, memo[i][1])

    out.append(str(memo[0][0]))

print("\n".join(out))
