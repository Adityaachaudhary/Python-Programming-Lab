def anagram(x,y):
    b = sorted(x)
    c = sorted(y)
    return b == c


ls1 = eval(input("enter list 1: "))
ls2 = eval(input("enter list 2: "))
count = 0 

for i in ls1:
    for j in ls2:
        if anagram(i,j):
            count +=1

print(count)