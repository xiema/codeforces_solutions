from collections import deque

n, m, s = map(int, input().strip().split())
s = str(s)
p, revp = {s: []}, {}
for _ in range(m):
    u, v = input().strip().split()
    p.setdefault(u, []).append(v)
    p.setdefault(v, [])
    revp.setdefault(v, []).append(u)

reachable = {v: set() for v in p}
def solve():
    q = deque([(r, r) for r in p[s]])
    while q:
        r, cur = q.popleft()
        reachable[cur].add(r)
        if len(reachable[cur]) > 1:
            return cur
        for v in p[cur]:
            if v != s and r not in reachable[v]:
                q.append((r, v))

def getpath(w, r):
    path = [w]
    while path[-1] != r:
        for u in revp[path[-1]]:
            if r in reachable[u]:
                path.append(u)
                break
    path.append(s)
    path.reverse()
    return path

w = solve()
if w:
    r1, r2 = list(reachable[w])
    path1, path2 = getpath(w, r1), getpath(w, r2)
    print(f"Possible\n{len(path1)}\n{' '.join(path1)}\n{len(path2)}\n{' '.join(path2)}")
else:
    print("Impossible")
