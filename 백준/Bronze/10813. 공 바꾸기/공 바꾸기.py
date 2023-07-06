N, M = map(int, input().split())
B = [i for i in range(1, N+1)]

for a in range(M):
    i, j = map(int,input().split())
    b = B[i-1]
    B[i-1] = B[j-1]
    B[j-1] = b
for d in range(N):    
    print(B[d], end =" ")