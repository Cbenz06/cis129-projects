#Author: Caleb Benzi
#CIS129 Module 3 Lab
#Receipt calculator for my Coffee and Muffin Shop

#Declare prices and tax amount

COFFEE_PRICE = 5
MUFFIN_PRICE = 4
DONUT_PRICE = 3
GOD_KILLER_PRICE = 999999
TAX = .06

#INPUT

print('***************************************\n')
print('My Coffee and Muffin and Donut and Power of God Shop\nNumber of coffees bought?')
coffeeBought = input()
print('Number of muffins bought?')
muffinsBought = input()
print('Number of donuts bought?')
donutsBought = input()
print('Number of God Killers bought?')
godsBought = input()
print('***************************************\n')

#PROCESSING

coffeeTotal = float(coffeeBought) * COFFEE_PRICE
muffinTotal = float(muffinsBought) * MUFFIN_PRICE
donutTotal = float(donutsBought) * DONUT_PRICE
godTotal = float(godsBought) * GOD_KILLER_PRICE
beforeTax = coffeeTotal + muffinTotal + donutTotal + godTotal
tax = beforeTax * TAX
receiptTotal = beforeTax + tax

#OUTPUT

print('\n***************************************\n')
print('My Coffee and Muffin and Donut and Power of God Shop Receipt')
print(str(coffeeBought) + ' Coffee at $5 each: $ ' + str(coffeeTotal) + '0')
print(str(muffinsBought) + ' Muffins at $4 each: $ ' + str(muffinTotal) + '0')
print(str(donutsBought) + ' Donuts at $3 each: $ ' + str(donutsTotal) + '0')
print(str(godsBought) + ' God Killers at $999999 each: $ ' + str(godTotal) + '0')
print('6% tax: $ ' + str(tax))
print('---------\n')
print('Total: $ ' + str(receiptTotal))
print('***************************************')
