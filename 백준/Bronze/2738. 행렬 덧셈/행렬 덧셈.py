# 행렬의 크기 N과 M 입력받기
N, M = map(int, input().split())

# 행렬 A 입력받기
A = []
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

# 행렬 B 입력받기
B = []
for _ in range(N):
    row = list(map(int, input().split()))
    B.append(row)

# 두 행렬을 더한 결과 행렬 계산
result = []
for i in range(N):
    result_row = []
    for j in range(M):
        result_row.append(A[i][j] + B[i][j])
    result.append(result_row)

# 결과 출력
for row in result:
    print(*row)