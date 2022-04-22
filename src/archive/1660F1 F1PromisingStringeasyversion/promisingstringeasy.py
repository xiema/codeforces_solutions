from collections import deque

t = int(input().strip())

out = []
for _ in range(t):
    n = int(input().strip())
    s = input().strip()
    q = deque()
    ans = 0

    for i in range(n):
        x = s[i]
        q.appendleft((int(x == '+'), int(x == '-'), 0, x == '-'))
        for j in range(1, len(q)):
            pc, mc, amc, tm = q[j]
            if x == '+':
                pc += 1
                tm = False
            else:
                mc += 1
                if tm:
                    amc += 1
                    tm = False
                else:
                    tm = True
            if pc == mc or (pc < mc and (mc - pc) % 3 == 0 and (mc - pc) // 3 <= amc):
                ans += 1
            q[j] = (pc, mc, amc, tm)

    out.append(str(ans))

print("\n".join(out))
