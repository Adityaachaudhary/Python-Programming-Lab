a = int(input('enter the shopping amount'))
if a>25000:
    print('Your category is GOLD')
    print ('amount to be paid is',a-(20/100)*a)
elif a>10000 and a<25000:
    print('Your category is Silver')
    print('amount to be paid is', a-(10/100)*a)
else:
    print('Your category is Bronze')
    print('Amount to be paid is', a-(5/100)*a)