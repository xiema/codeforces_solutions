from collections import deque

n = int(input().strip())
a = list(map(int, input().strip().split()))

memo = {0: 0, 32768: 0}
q = [32768]

i = 1
while q:
    _q = []
    for x in q:
        y = x - 1
        if y >= 0 and y not in memo:
            memo[y] = i
            _q.append(y)
        y = x // 2
        if x % 2 == 0 and y not in memo:
            memo[y] = i
            _q.append(y)
        if (32768 - x) % 2 == 0:
            y = 32768 - (32768 - x) // 2
            if y not in memo:
                memo[y] = i
                _q.append(y)
    q = _q
    i += 1

print(" ".join([str(memo[i]) for i in a]))
