numberOfDaysWorked = int( input( "How Many Days Worked? "))
totalNumberOfPennies = 0
print()
print( "Day(s)\tSalary(In Pennies)\n----\t-------" )
for currentDay in range( numberOfDaysWorked ):
    penniesForTheDay = 2 ** currentDay
    totalNumberOfPennies += penniesForTheDay
    print( currentDay + 1, "\t" , penniesForTheDay )
totalPay = totalNumberOfPennies * 0.01
print( "\nFinal Pay = $", totalPay, sep = "" )