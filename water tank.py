r = 5
h = 10
F = 15
t = int(input( ))
Vw = F * t
Vt = 3.14 * r ** 2 * h
if Vw < Vt:
    print('Underflow')
    ht = Vw/ (3.14 *r **2)
    HT = round(ht,2)
    hr = h -ht
    HR = round(hr,2)
    print('Filled height',HT)
    print('Remaining height',HR)
elif Vw>Vt:
    print('Overflow')
    print('Volume',Vw-Vt)
else:
    print('Tank Full')
    
    