t = int(input().strip())

def solve(table, n, m):
    for i in range(n - 1):
        for j in range(m - 1):
            if table[i][j] + table[i][j+1] + table[i+1][j] + table[i+1][j+1] == 3:
                return False
    return True

out = []
for _ in range(t):
    n, m = map(int, input().strip().split())
    table = []
    for _ in range(n):
        table.append(list(map(int, input().strip())))

    out.append("YES" if solve(table, n, m) else "NO")

print("\n".join(out))
