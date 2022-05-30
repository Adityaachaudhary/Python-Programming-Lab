'''there is a string of digits only. sort the strings so that all the prime digits come forward the prime 
digits will be arranged in lexicographical order'''


def isprime(x):
    count = 0 
    for i in range(1,x+1):
        if (x % i) == 0:
            count += 1
    return count == 2
str = eval(input())
ls1 = []
ls2 = []
for i in str:
    if (isprime(i)):
        ls1.append(i)
    else:
        ls2.append(i)
ls1.sort()
re = ls1 + ls2
out = ''.join(re)
print(f'''{out}''')
        