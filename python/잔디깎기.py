N: int = 5
M: int = 5

x = [0] * N
y = [0] * M
H = []

result = "YES"

for i in range(N):
    H.append(list(map(int, input().split())))

    for j in range(M):
        x[i] = max(x[i], H[i][j])
        y[j] = max(y[j], H[i][j])

for i in range(N):
    for j in range(M):
        if H[i][j] < x[i] and H[i][j] < y[j]:
            result = "NO"
            break
    if result == "NO":
        break

print(result)
