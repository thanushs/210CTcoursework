intString = str(input("Enter a string: "))

def vowels(intString):
    if len(intString) == 0:
        return intString
    elif (intString[0] in "aeiouAEIOU"):
        return vowels(intString[1:])
    return (intString[0] + vowels(intString[1:]))
print(vowels(intString))
