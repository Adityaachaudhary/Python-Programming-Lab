a = int(input('enter the side a of triangle'))
b = int(input('enter the side b of triangle'))
c = int(input('enter the side c of triangle'))
if a<=0 or b<=0 or c<=0 or a+b<=c or a+c<=b or b+c<=a:
    print('invalid')
else:
    if a!=b and a!=c and b!=c:
        print('triangle is scalene')
    elif a==b or a==c or b==c:
        print('triangle is isso')
    elif (a**2 ==b**2 + c**2) or (b**2 ==a**2 + c**2) or (c**2 ==a**2 + b**2):
        print('triangle is right angled')
    else:
        print('invalid input')