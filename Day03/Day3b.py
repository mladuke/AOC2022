import string

#open input file and assign to object f
f = open("Day03/input3.txt","r")
alpha=' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
total = 0


for line1 in f:
    line2 = f.readline()
    line3 = f.readline()
    aset =set(line1)
    bset =set(line2)
    cset =set(line3)
    same= aset & bset & cset
    same.remove('\n')
    sameSt = ''.join(same)
    numValue = alpha.find(sameSt)
    print (line1,line2,line3, same,numValue )
    total +=numValue

print(total)

#Answer 2581