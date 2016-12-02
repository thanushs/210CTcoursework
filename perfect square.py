value = int(input("Enter a value: "))
squareNumber = 1
count = 1
while squareNumber <= value:
    squareNumber = count ** 2
    count = count + 1
   
    
if squareNumber > value:
        squareNumber = (count - 2) ** 2
print("The highest perfect square number is " + str(squareNumber))

