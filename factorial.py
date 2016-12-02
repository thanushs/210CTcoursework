x = 0
while x == 0:
    factorialInput = int(input("Enter a factorial value: "))
    total = 1
    noOfZeros = 0
    count = factorialInput
    if factorialInput > 0:
        while count > 1:
            total = total * count * (count - 1)
            count = count - 2
            
        print (total)
        total = str(total)
        for i in total:
            if i == "0":
               noOfZeros = noOfZeros + 1
               

    print("The number of zeros in " + str(factorialInput) + " factorial is " + str(noOfZeros))
    print("")


