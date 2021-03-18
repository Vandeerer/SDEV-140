print("Prime Value List - Taylor Griffin")
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
    for currentValue in range(1, 100):
        if isPrime(currentValue):
            print(currentValue, end=" ")
main()
