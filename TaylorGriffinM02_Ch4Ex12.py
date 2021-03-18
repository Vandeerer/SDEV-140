userInterger = int( input( "Please enter a number: " ) )
while userInterger < 1:
    userInterger = int( input("Please enter a positive number please: ") )
factorial = 1
for currentNumber in range(1, userInterger + 1 ):
    factorial = factorial * currentNumber
print()
print( "The factorial of", userInterger, "is", factorial )