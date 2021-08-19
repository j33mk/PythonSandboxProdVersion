sum = 0

while True:
    print('Enter Items (Enter 0 to End) ')
    while True:
        k = float(input('Enter cost of item:: '))
        sum =sum+k
        if k == 0:
            break
    print('Total is: '+str(sum))
    salesTax = round(sum*0.06,2)
    print('Sales Tax is: '+str(salesTax))
    afterTax = round(sum+salesTax,2)
    print('Total Ater Tax is: '+str(afterTax))
    choice = input('Do you want to continue again? (y/n):: ')
    if choice == 'y':
        continue
    elif choice == 'n':
        print('Thanks, bye!')
        break
