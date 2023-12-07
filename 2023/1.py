import re
with open("2023\inputs\input1.txt", 'r') as f:
    lines = f.readlines()
total = 0
for i in lines:
    nums = re.findall(r'\d', i)
    total += int(nums[0] + nums[-1])
print(total)

