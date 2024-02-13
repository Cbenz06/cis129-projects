#Author: Caleb Benzi
#CIS129 Module 3 Lab
#Receipt calculator for my Coffee and Muffin Shop

#Declare prices and tax amount

COFFEE_PRICE = 5
MUFFIN_PRICE = 4
TAX = .06

#INPUT

print('***************************************\n')
print('My Coffee and Muffin Shop\nNumber of coffees bought?')
coffeeBought = input()
print('Number of muffins bought?')
muffinsBought = input()
print('***************************************\n')

#PROCESSING

coffeeTotal = float(coffeeBought) * COFFEE_PRICE
muffinTotal = float(muffinsBought) * MUFFIN_PRICE
beforeTax = coffeeTotal + muffinTotal
tax = beforeTax * TAX
receiptTotal = beforeTax + tax

#OUTPUT

print('\n***************************************\n')
print('My Coffee and Muffin Shop Receipt')
print(str(coffeeBought) + ' Coffee at $5 each: $ ' + str(coffeeTotal) + '0')
print(str(muffinsBought) + ' Muffins at $4 each: $ ' + str(muffinTotal)+ '0')
print('6% tax: $ ' + str(tax))
print('---------\n')
print('Total: $ ' + str(receiptTotal))
print('***************************************')
