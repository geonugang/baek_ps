# 정수 N 입력
N = int(input())

sum_ = 0
triple_ =0

# 1부터 N까지의 합
for a in range(1,N+1):
    sum_ += a

# 1부터 N까지의 세제곱의 합
for b in range(1, N+1):
    triple_ += b*b*b
print(sum_)        # 1부터 N까지의 합
print(sum_*sum_)   # 1부터 N까지의 합의 제곱
print(triple_)     # 1부터 N까지의 세제곱의 합