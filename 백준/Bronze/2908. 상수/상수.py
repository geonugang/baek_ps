num = []
A, B = map(int, input().split())
reverse_num1 = int(str(A)[::-1])
reverse_num2 = int(str(B)[::-1])
num.append(reverse_num1)
num.append(reverse_num2)
print(max(num))