def floor_function (a=0,b=0):
    c = 0
    while a>=b:
        a-=b
        c +=1
    return c

a,b = list(map(int,input().split))
out = floor_function(a,b)
print(out)

    