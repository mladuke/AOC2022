#open input file and assign to object f
f = open("Day01/input1.txt","r")
# calstotal is for a given elf
calstotal = 0
# maxcals is the greatest number of cals detected so far
maxcals = 0
#elfcount is just for debugging
elfcount = 0
for line in f:
    # Detect if line is empty
    if line.split(): 
        #convert non empty line to an integer so comparsions and arithmetic
        if (int(line)>0):
            #running count of total cals for elf
            calstotal +=int(line)
    else:
        #blank line so detect if total cals is greater than previous maxcals, update maxcals if it is
        elfcount += 1
        #print(elfcount,calstotal)
        if calstotal > maxcals:
            maxcals = calstotal
            print("Newmax",maxcals, elfcount)
        #Blank line means new elf is next    
        calstotal = 0
#processing for last elf in no blank line at End of file
elfcount +=1
#print(elfcount,calstotal)
if calstotal > maxcals:
    maxcals = calstotal
    print("Newmax",maxcals,elfcount)
print (maxcals)

#Output of Program
# Newmax 58522 1
# Newmax 62043 10
# Newmax 66172 18
# Newmax 70698 65
# 70698