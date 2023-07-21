num = {2:['A','B','C'], 3:['D','E','F'], 4:['G','H','I'], 5:['J','K','L'], 6:['M','N','O'], 7:['P','Q','R','S'],
       8:['T','U','V'], 9:['W','X','Y','Z']}
sum_time = 0
word = input()
for i in range(len(word)):
    for key in num:
        if word[i] in num.get(key,[]):
            sum_time += key + 1
print(sum_time)