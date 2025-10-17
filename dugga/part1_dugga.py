numbers = [15, -5, -12, 7, 10, -7, 3, -10, 4]
#A
sum = 0
for n in numbers:
    if abs(n) >= 10:
        sum += n
print(sum) #adds numbers without absolute value but not specified if it should be?
#B
cube = []
for c in numbers:
   if c < 0:
     cube.append(c ** 3)
print(cube)
#C 
#used ai to suggest where abs(n) should be placed in my code. 
#i know code is correct because i did it in practice dugga.
#and the output gives me 7 which I know is the first repeat left to right.
seen = set()
duplicate = None
for d in numbers:
    if abs(d) in seen:
        duplicate = abs(d)
        break
    seen.add(abs(d))
print(duplicate)