basket = 0
keepshopping = 'yes'
while keepshopping == 'yes':
    item = float(input('Enter price of item: '))
    basket = basket + item
    keepshopping = input('Do you wish to keep shopping? (yes/no?) ')

print('You spent basket', basket)
