numberList = []
count = 0
finalNumberList = []
finalNumberList2 = []
x = 'yes'
while x == 'yes':
  numberList.append(int(input("Enter an integer: ")))
  x = str(input("Do you want to add another number? "))
print(numberList)
for i in range(len(numberList)):
    finalNumberList.append(numberList[i])
    if i ==len(numberList)- 1 or numberList[i] > numberList[i+1] :      
        if len(finalNumberList) > len(finalNumberList2):
            finalNumberList2 = finalNumberList
            finalNumberList=[]
        else:
            finalNumberList2 = finalNumberList2
        print(finalNumberList, finalNumberList2)
print(finalNumberList2)
  

