total_purchased = float(input('Amount of Packages Purchased?'))
price = 99
if total_purchased < 10:
    discount = 0
elif total_purchased < 20:
    discount = 0.1
elif total_purchased < 50:
    discount = 0.2
elif total_purchased < 100:
    discount = 0.3
else:
    discount = 0.4
subtotal = total_purchased * price
discount_amount = subtotal * discount
final_price = subtotal - discount_amount
print('\nSubtotal: $', format(subtotal, '10,.2f'), \
'\nDiscount: $', format(discount_amount, '10,.2f'), \
'\nFinal Price: $', format(final_price, '10,.2f'), sep='')