T = int(input())
result = []
for a in range(T):
    R, S = input().split()
    for i in range(len(S)):
        print(S[i]*int(R),end='')
    print()