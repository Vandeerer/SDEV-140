print("Average Steps Taken - Taylor Griffin")
month = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
def main():
    steps()
def steps():
    stepCounter = open('steps.txt', 'r')
    monthCounter = 0
    for num in range(1, 13):
        total = 0
        count = 0
        average = 0
        for count in range(1, days[monthCounter] + 1):
            steps = int(stepCounter.readline())
            total = total + steps
        average = total / days[monthCounter]
        print ("In "+month[monthCounter]+' you took '+format(int(average))+" steps!")
        monthCounter = monthCounter + 1
main()
print("Keep Up The Good Work! Change WILL Happen!")
