N = int(input())
grade = list(map(int, input().split()))
NewScores = []
 
M = max(grade)

for b in grade:
    new = (b / M*100)
    NewScores.append(new)
    
print(sum(NewScores)/N)