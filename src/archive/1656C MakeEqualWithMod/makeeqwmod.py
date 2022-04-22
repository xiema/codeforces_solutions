t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    a = list(set(map(int, input().strip().split())))
    a.sort()

    if len(a) == 1:
        print("YES")
    elif a[0] == 1 or a[1] == 1:
        if a[0] == 0:
            print("NO")
        else:
            for i in range(1, len(a)):
                if a[i] - a[i-1] == 1:
                    print("NO")
                    break
            else:
                print("YES")
    else:
        print("YES")
