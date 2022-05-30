p = eval(input('enter the principle'))
r = eval(input('enter the rate of intrest'))
t = int(input('enter the time'))
SI = p*r*t/100
amt = p+SI
print('the SI is',SI)
print('the amount is',amt)