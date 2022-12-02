#open input file and assign to object f
f = open("Day02/input2.txt","r")
score = {"X":1,
         "Y":2,
         "Z":3,
         "AX":3,
         "AY":6,
         "AZ":0,
         "BX":0,
         "BY":3,
         "BZ":6,
         "CX":6,
         "CY":0,
         "CZ":3
         }
total = 0
for line in f:
    e1=line[0]
    e2=line[2]
    result=e1+e2
    linetotal = score[e2]+score[result]
    total +=linetotal
    print(e1,e2,score[e2],score[result],linetotal,total)
print(total)

#Answer 15572