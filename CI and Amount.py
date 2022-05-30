p = eval(input('enter the principle'))
r = eval(input('enter the rate of intrest'))
t = int(input('enter the time'))
amt = p * ((1 + r/100)**t)
ci = amt - p 
print('the CI is', ci)
print('the amount is',amt)