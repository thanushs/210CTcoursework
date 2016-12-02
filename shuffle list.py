import random
x = 'yes'                                   
intList = []                                
while x == 'yes':                           
    y = int(input('Enter a number: '))      
    intList.append(y)                       
    x = input("Do you want to continue? ")  
print(intList)                              
count = 0                                   
maxNumber = (len(intList)-1)                
minNumber = 0                               
for i in intList:                           
    randomNumber = random.randrange(minNumber, maxNumber)
    if randomNumber == count:
        randomNumber = random.randrange(minNumber, maxNumber)
    intList[count], intList[randomNumber] = intList[randomNumber], intList[count]
    count = count + 1
print(intList)
            
