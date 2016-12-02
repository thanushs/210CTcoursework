intString = str(input("Enter the sentence: "))
finalStringList = []
newString = ""
newStringList = []
for c in intString:
    if c == ' ':
        newStringList.append(newString)
        newString = ''
    else:
        newString += c
if newString:
    newStringList.append(newString)
count = len(newStringList) - 1
while count >= 0:
    x = newStringList[count]
    finalStringList.append(x)
    count = count - 1

finalString = " ".join(finalStringList)
print(finalString)
