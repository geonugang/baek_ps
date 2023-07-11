N = int(input())
grade = input().split()
NewScores = []

for a in range(N):
    grade[a] = int(grade[a])  
M = max(grade)

for b in grade:
    new = (b / M*100)
    NewScores.append(new)
    
print(sum(NewScores)/N)