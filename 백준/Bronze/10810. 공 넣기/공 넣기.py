N, M = map(int, input().split())
B = []
for a in range(N):
    B.append(0)
for b in range(M):
    i, j, k = map(int, input().split())
    for c in range(i-1, j):
        B[c] = k

for d in range(N):
    print(B[d], end = " ")