# Tip Tax and Total
# 6/6/17
# CTI110 M2HW2 - Tip Tax Total
#Michael Winkler
#

foodCharge = float(input('Please enter the charge of the food: '))
tip = 0.18 * foodCharge
salesTax = 0.07 * foodCharge
print('Food Charge: $' + format( foodCharge, ",.2f"), "Tip: $" + \
format( tip, ",.2f" ), 'Sales Tax: $' + format( salesTax, ',.2f'),\
'Total: $'+ format(foodCharge ',.2f"), sep = "\n")
