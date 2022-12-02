#open input file and assign to object f
f = open("Day02/input2.txt","r")
score = {"X":1,
         "Y":2,
         "Z":3,
         "AX":3,
         "AY":4,
         "AZ":8,
         "BX":1,
         "BY":5,
         "BZ":9,
         "CX":2,
         "CY":6,
         "CZ":7
         }
total = 0
for line in f:
    e1=line[0]
    e2=line[2]
    result=e1+e2
    total +=score[result]
    print(e1,e2,score[result],total)
print(total)

#Answer 16098