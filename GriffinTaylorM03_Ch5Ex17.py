print("Prime Values - Taylor Griffin")
def isPrime(userValue):
    evenDivisions = 0
    if userValue <= 1:
        return False
    for currentValue in range(1, userValue + 1):
        if userValue % currentValue == 0:
            evenDivisions = evenDivisions + 1
            if evenDivisions > 2:
                return False
    return True
def main():
    userValue = int(input("Enter a number to determine if it is a prime number - "))
    print()
    if isPrime(userValue):
        print(userValue, "is prime")
    else:
        print(userValue, "is not prime")
main()
