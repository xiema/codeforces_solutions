from sys import stdin, stdout

t = int(input().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    a = list(map(int, stdin.readline().strip().split()))
    b, e, mx = n, n, 0
    i = 0
    while i < n:
        if a[i] == 0 or a[i] == 1:
            i += 1
            continue
        s, t = 0, 0
        j = i
        while j < n:
            if a[j] == 0:
                break
            s += (a[j] < 0)
            t += (abs(a[j]) > 1)
            if s % 2 == 0 and t > mx:
                mx = t
                b, e = i, j + 1
            j += 1
        while i < j and s % 2 and t > mx:
            s -= (a[i] < 0)
            t -= (abs(a[i]) > 1)
            i += 1
            if s % 2 == 0 and t > mx:
                mx = t
                b, e = i, j
        i = j


    stdout.write(f"{b} {n - e}\n")
