n = int(input("Enter a number: "))
count = n - 1
answer = ''

def primeCheck (n, count, answer):
    while answer == '' and count > 1:
        if (n % count == 0):
            answer = (str(n) + " is not a prime number")
            return (answer)
        count = count - 1
        if count == 1:
            answer  = (str(n) + " is a prime number")
            return(answer)   

output = primeCheck(n, count, answer)
print(output)
