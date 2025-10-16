
nums = [3, 8, 0, -2, 11, 6, 6]
#A
sum = 0
for n in nums:
    if n % 2 == 0:
        sum += n
print(sum)
#B
square = []
for s in nums:
   if s > 0:
     square.append(s ** 2)
print(square)
#C
appended = []
duplicate = None
for d in nums:
    if d in appended == d:
        break
appended.append(d)
print(appended)