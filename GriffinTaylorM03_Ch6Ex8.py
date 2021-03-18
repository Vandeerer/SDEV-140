print("Random Number File Reader - Taylor Griffin")
def displayNumbers(fileToBeRead):
    try:
        randomNumbersFile = open(fileToBeRead, "r")
        numberOfRandomNumbers = 0
        total = 0
        line = randomNumbersFile.readline()
        while line != "":
            numberOfRandomNumbers += 1
            randomNumber = int(line)
            total += randomNumber
            print(randomNumber)
            line = randomNumbersFile.readline()
    except Exception as Error:
        print("Error Encountered!", Error)
    else:
        print("\nTotal = "+str(total)+"\nDifferent Numbers = "+str(numberOfRandomNumbers))
        randomNumbersFile.close()
    finally:
        print("\nEnd of the program")
def main():
    displayNumbers("randomNumbers.txt")
main()
