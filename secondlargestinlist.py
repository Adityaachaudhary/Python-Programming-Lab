a=[]
n=int(input("enter no. of elements"))
for i in range(1,n+1):
    b=int(input("enter element"))
    a.append(b)
a.sort()
print("largest no. is ",a[n-2])