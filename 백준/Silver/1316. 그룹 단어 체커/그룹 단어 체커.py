N = int(input())
cnt = N

for a in range(N):
    word = input()
    for b in range(len(word)-1):
        if word[b] == word[b+1]:
            continue
        elif word[b] in word[b+1:]:
            cnt -= 1
            break

print(cnt)