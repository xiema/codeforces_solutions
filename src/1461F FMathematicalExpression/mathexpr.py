from sys import stdin

n = int(stdin.readline().strip())
as = stdin.readline().split()
a = map(int, as)
s = stdin.readline().strip()

if len(s) == 1:
    print(s.join(as))
elif '+' in s and '-' in s:
    print('+'.join(as))
elif '-' in s and '*' in s:
    for i in range(len(a)):
        if a[i] == 0:
            out = []
            if i > 0:
                out.append('*'.join(as[:i]))
            if i < len(a)-1:
                out.append('*'.join(as[i+1:]))
            print('-'.join(out))
            break
    else:
        print('*'.join(as))
elif '+' in s and '*' in s:
    gs = []
    i, j = 0, 1
    p = a[i]
    while i < len(a) and j < len(a):
        if a[i] <= 1 or a[j] <= 1:
            if a[j] != a[i]:
                gs.append((p, j-i))
                i = j
            p = a[j]
        else:
            p *= a[j]
        j += 1
    else:
        if i < len(a):
            gs.append((p, j-i))

    i, j = 0, 1
    while i < len(g) and j < len(g):
        
