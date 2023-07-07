nums = []
for i in range(10):
    a = int(input())
    b = a%42
    
    if int(b) in nums:
        pass
    else:
        nums.append(b)
print(len(nums))