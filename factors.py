factors = {}

for num in range (1,6+1): #each num as the key for each row
    start = 0 #for each column in the matrix, starts as 0
    for factor in range (1,num+1):#go through each number upto the key to test if a factor
        
        if num % factor == 0:
            factors[(num,start)] = factor # if a factor, assign it to the position in dictionary
            start += 1 # and the column number goes up 1
                       
        else:
            continue # if not a factor, go to the next cycle to test the next number 
            
print(factors)            
for i in range(6+1):
    for j in range(6+1):
        print(factors.get((i, j), 0), "", end = '')
    print()            
    