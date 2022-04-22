t = int(input().strip())

def checkpalin(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i, j = i + 1, j - 1
    return True

def solve(n, s):
    i, c = 0, 0
    while i < n:
        if i == n - 1:
            break
        if s[i] == '(':
            c += 1
            i += 2
        else:
            for j in range(i + 1, n):
                if checkpalin(s, i, j):
                    c += 1
                    i = j + 1
                    break
            else:
                break

    return c, max(0, n - i)

for _ in range(t):
    n = int(input().strip())
    s = input().strip()

    c, r = solve(n, s)
    print(c, r)
