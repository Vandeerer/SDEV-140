#Sales Tax v1.0 - Taylor Griffin
print('Sales Tax Calculator by Taylor Griffin')
#this is where the tax is calculated and the price is entered
base_purchase = float(input('Please Enter the Price of your Purchase:'))
county_tax = base_purchase * 0.025
state_tax = base_purchase * 0.05
total_purchase = base_purchase+county_tax+state_tax
#display the taxes and amount paid
print('Base Price: $', "{:.2f}".format(base_purchase))
print('County Tax: $', "{:.2f}".format(county_tax))
print('State Tax: $', "{:.2f}".format(state_tax))
print('Final Price after Tax: $', "{:.2f}".format(total_purchase))