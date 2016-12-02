x = "yes"
intList = []
count = 0
low = 10
high = 14
answer = "False"
while x == "yes":
    a = int(input("Enter a number: "))
    intList.append(a)
    x = input("Do you want to continue? ")
intList.sort(key=int)
print(intList)
while len(intList) > 0 and answer == "False":
    if (len(intList) % 2) == 0:
        count = len(intList)
    else:
        count = len(intList) + 1

    count = int((count / 2) - 1)
    if intList[count] >= low and intList[count] <= high:
        answer = "True"
    elif intList[count] < low:
        del intList[:count]
        
    else:
        del intList[count:]

print(answer)
