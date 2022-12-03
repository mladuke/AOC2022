def splitString(string):
    first_half = string[0:len(string)//2]
    second_half = string[len(string)//2:]
    return [first_half,second_half]

#open input file and assign to object f
f = open("Day03/input3.txt","r")
import string

alpha=' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

total = 0

for line in f:
    a,b = splitString(line)
    aset =set(a)
    bset =set(b)
    same= aset & bset
    sameSt = ''.join(same)
    numValue = alpha.find(sameSt)
    print (line,a,b, aset, bset, same,numValue )
    total += numValue
print(total)

#Answer 7550