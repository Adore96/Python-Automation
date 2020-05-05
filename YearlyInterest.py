years = input('How many years will you be saving?  ')
principal = input('How much money is there currently?  ')
monthinvestment = input('How much do u think you can invest per monthly? ')
interest = input('How much do you estimate will be the yearly interest of this investment? (10% = 0.1) ? ')

print(' ')

monthinvestment = monthinvestment*12
final_amount = 0

for i in range(0,years):
    if final_amount==0 :
        final_amount == principal

    final_amount = (final_amount+monthinvestment)*(1+interest)

print('This is how much you would have after {} years :'.format(years)+str(final_amount))
