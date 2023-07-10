N, M = map(int, input().split())
B = []
for a in range(N):
    B.append(a+1)
for b in range(M):
    i, j= map(int, input().split())
    re = B[i-1:j]
    re.reverse()
    B = B[:i-1] + re + B[j:]
    
print(*B)