print("Average of Numbers - Taylor Griffin"+"\nPlease Make Sure the Working Directory is Set Correctly and 'numbers.txt' is in the Same Folder as this Script!")
def main():
    try:
        numbersFile = open("numbers.txt", "r")
        total = 0
        numberOfLines = 0
        line = numbersFile.readline()
        while line != "":
            numberOfLines += 1
            total += int( line )
            line = numbersFile.readline()
            average = total / numberOfLines
    except IOError as error:
            print("An IOError has occured")
    except ValueError as error:
            print("A ValueError has occured")
    else:
        print("Average of 'numbers.txt' is ", average)
main()
