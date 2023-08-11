N = int(input())                        # 단어의 개수 N을 입력
cnt = N

for a in range(N):                      # N번 반복
    word = input()                      # 단어 입력
    for b in range(len(word)-1):        # 0번째부터 단어의 알파벳 개수-1 만큼 반복
        if word[b] == word[b+1]:        # word의 b번째 알파벳과 b+1번째 알파벳이 같은 경우 continue
            continue                    
        elif word[b] in word[b+1:]:     # word의 b번째 알파벳이 b+1번째 이후에 같은 알파벳이 나온다면 
            cnt -= 1                    # 그룹단어가 아니기에 cnt에서 -1
            break

print(cnt)