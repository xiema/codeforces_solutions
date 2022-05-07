from sys import stdin, stdout

n = int(stdin.readline().strip())
A = stdin.readline().split()
s = stdin.readline().strip()

if s in ["+", "-", "*"]:
    print(s.join(A))
elif s in ["+-", "-+"]:
    print('+'.join(A))
elif '+' in s:
    a = list(map(int, A))
    l = len(a)
    P = [i - 1 for i in range(l)]

    def solve(a, b, e, P):
        l = e - b
        if l < 1:
            return

        cnt, p = 0, 1
        gb, ge = e, b
        mn = 9
        for i in range(l):
            if a[i + b] > 1:
                cnt += 1
                p *= a[i + b]
                mn = min(a[i+b], mn)
                gb = min(i + b, gb)
                ge = max(i + b + 1, ge)
        if cnt == 0:
            return
        if p >= p // mn + (ge - gb - cnt) + mn:
            P[ge-1] = gb - 1
            return




        M = [0] * l

        for i in range(l):
            if a[i + b] == 1:
                M[i] = M[i-1] + 1
                continue
            p = a[i + b]
            if i > 0:
                M[i] = M[i-1] + p
            else:
                M[i] = p
            for j in range(i-1, -1, -1):
                p *= a[j + b]
                if j > 0:
                    mx = M[j-1] + p
                else:
                    mx = p
                if M[i] < mx:
                    M[i] = mx
                    P[i+b] = j - 1 + b

    i, j = 0, 0
    while j < l:
        if a[j] == 0:
            solve(a, i, j, P)
            i = j = j + 1
        else:
            j += 1
    else:
        solve(a, i, j, P)

    ops = ['+' for _ in range(l - 1)] + ['']
    i = l - 1
    while i >= 0:
        for j in range(i-1, P[i], -1):
            ops[j] = '*'
        i = P[i]

    for x, y in zip(A, ops):
        stdout.write(x)
        stdout.write(y)

else:
    for i in range(len(A)):
        if A[i] == '0':
            out = []
            if i > 0:
                out.append('*'.join(A[:i]))
            out.append('*'.join(A[i:]))
            print('-'.join(out))
            break
    else:
        print('*'.join(A))
