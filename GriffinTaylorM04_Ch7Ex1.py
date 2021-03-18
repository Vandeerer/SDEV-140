print("Total Sales by Taylor Griffin")
dailySales = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
daysOfWeek = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
totalSales = 0.0
for i in range(len(dailySales)):
    dailySales[i] = float(input("Enter the sales for " + daysOfWeek[i]+": $"))
    totalSales += dailySales[i]
print("Sales Per Day: ", dailySales)
print("The total sales for the week was: $", format(totalSales, ".2f"))
