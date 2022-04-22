t = int(input().strip())

for _ in range(t):
    s = input().strip()
    c = 0
    letters = set()
    for x in s:
        if x in letters:
            c += len(letters) - 1
            letters.clear()
        else:
            letters.add(x)
    c += len(letters)
    print(c)
