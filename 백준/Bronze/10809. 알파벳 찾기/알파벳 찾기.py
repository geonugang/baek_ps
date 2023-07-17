strs = input()
apb = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(apb)):
    if apb[i] in strs:
        print(strs.find(apb[i]), end=' ')
    else:
        print(-1, end=' ')