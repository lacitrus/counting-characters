
#Create a function factors that takes in an integer n and generates a dictionary that contains the factors of all values from 1 to n. 
#A factor is any number that evenly divides another number. For example, the factors of 6 are 1, 2, 3, and 6. Factors of 15 are 1, 3, 5, 
#and 15. The keys of your dictionary should be an integer between 1 and n and the values should be a list of factors for that particular 
#key.


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

#Print the matrix as a sparse matrix, return factors when it exists or return 0 when there is no value in the spot
#"", end = '' and print() in next line is for formating the matrix only.
for i in range(6+1):
    for j in range(6+1):
        print(factors.get((i, j), 0), "", end = '')
    print()            
    
