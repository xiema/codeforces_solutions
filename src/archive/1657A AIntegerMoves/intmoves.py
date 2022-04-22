from math import sqrt

t = int(input().strip())

triples = set()
for i in range(51):
    for j in range(i + 1, 51):
        if sqrt(i * i + j * j) % 1 == 0:
            triples.add((i, j))

out = []
for _ in range(t):
    x, y = map(int, input().strip().split())
    if x > y:
        x, y = y, x
    if x == 0 and y == 0:
        out.append("0")
    elif (x, y) in triples:
        out.append("1")
    else:
        out.append("2")

print("\n".join(out))
