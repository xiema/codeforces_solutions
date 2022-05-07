n, m = map(int, input().strip().split())

ic, jc = {}, {}
for i in range(n):
    C = list(map(int, input().strip().split()))
    for j, c in enumerate(C):
        if c not in ic:
            ic[c], jc[c] = {}, {}
        ic[c][i] = ic[c].get(i, 0) + 1
        jc[c][j] = jc[c].get(j, 0) + 1

def total(C):
    total = 0
    for c in C.values():
        prev, prevCount, acc = None, 0, 0
        for k, v in sorted(c.items()):
            if prev is None:
                prev, prevCount = k, v
            else:
                acc += prevCount * (k - prev)
                total += acc * v
                prev, prevCount = k, prevCount + v
    return total

print(total(ic) + total(jc))
