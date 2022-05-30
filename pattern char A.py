h = int(input())
l = int(input())
k = 0

for i in range (1,h+1):
    for j in range(h-i):
        print(" ",end="")
    while 2 * i - 1 > k:
        if k ==0 or k ==2 * i -2 or i == l:
            print("*",end="")
        else:
            
            print(" ", end="")
        k += 1 
    print()
    k = 0
    