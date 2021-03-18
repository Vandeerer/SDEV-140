#Coumpound Interest Calculator by Taylor Griffin
print('Compound Interest Calculator by Taylor Griffin')
#All the values as inputs
P = float(input('Enter the Original/Principal Amount: $'))
r = float(input('Enter the Interest Rate: %'))
n = float(input('Enter the Amount of Times Interest will be Compounded in a Year: '))
t = float(input('Enter the Amount of Time in Years: '))
#the interest calculation
A = P*(((1+((r/100.0)/n))**(n*t)))
#Displays the Output
print('Final Amount After Interest: $', "{:.2f}".format(A))


