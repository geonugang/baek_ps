submit = []
none = []
for a in range(28):
    submit.append(int(input()))
    
for b in range(1,31):
    if (b in submit):
        continue
    else:
        none.append(b)
print(none[0])
print(none[1])