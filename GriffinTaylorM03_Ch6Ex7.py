print("Random Number File Writer - Taylor Griffin")
import random
def generateRandomNumber():
    randomNumber = random.randint(1,500)
    return randomNumber
def main():
    try:
            fileToBeWrittenTo = open("randomNumbers.txt", "w")
            numberOfRandomNumbers = int( input("Enter the Amount of Random Numbers You Would Like to Generate - "))
    except:
        print("An error has occured")
    else:
        for randomNumberCount in range(1, numberOfRandomNumbers + 1):
            randomNumber = generateRandomNumber()
            fileToBeWrittenTo.write(str(randomNumber )+"\n")
    finally:
        fileToBeWrittenTo.close()
        print("Numbers Written to 'randomNumbers.txt' Succesfully!")
main()
