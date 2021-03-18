#Cookie Recipe Calculator by Taylor Griffin
print('Cookie Recipe Calculator by Taylor Griffin')
#the values
cookie_amount = int(input('\nHow Many Cookies Do You Wish to Make? '))
cookies = 48
sugar = 1.5
butter = 1
flour = 2.75
#calculating the ingredients needed
total_sugar = (sugar * cookie_amount) /cookies
total_butter = (butter * cookie_amount) /cookies
total_flour = (flour * cookie_amount) /cookies
#Displaying the cups of ingredients needed formatted to the thousandths
print('\nNumber of Cookies =', cookie_amount, end='\n\n')
print('Cups of Sugar Needed =', format(total_sugar, ',.3f'))
print('Cups of Butter Needed =', format(total_butter, ',.3f'))
print('Cups of Flour Needed =', format(total_flour, ',.3f'), end='\n\n')