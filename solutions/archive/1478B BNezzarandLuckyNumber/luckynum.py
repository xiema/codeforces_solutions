from sys import stdin, stdout

t = int(stdin.readline().strip())

memo = {n : {} for n in range(1, 10)}
def check(d, n):
    if n < d:
        return False
    if n > d * 10 or n % d == 0:
        return True
    if n not in memo[d]:
        memo[d][n] = check(d, n-10)
    return memo[d][n]

for _ in range(t):
    _, d = map(int, stdin.readline().split())
    qs = map(int, stdin.readline().split())
    for q in qs:
        if check(d, q):
            stdout.write("YES\n")
        else:
            stdout.write("NO\n")
