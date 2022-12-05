#open input file and assign to object f
f = open("Day04/input4.txt","r")
total = 0

for line in f:
    lineSt = str(line)
    a,b = lineSt.split(',')
    a1,a2 = a.split('-')
    b1,b2 = b.split('-')
    a1i = int(a1)
    a2i = int(a2)
    b1i = int(b1)
    b2i = int(b2)
    a1,a2,b1,b2 =a1i,a2i,b1i,b2i
    total += 1
    if (a2<b1) or (b2<a1):
        total -= 1
print(total)

#Answer 794