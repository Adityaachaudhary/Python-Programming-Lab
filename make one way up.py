'''Write a complete program that takes an array A of an integer as input and displays 
True if the absolute difference between each adjacent pair of elements strictly increases otherwise False.'''

n = int(input())
lst = list(map(int, input().split()))
d1 = abs(lst[0]-lst[1])

for i in range (1 , n-1):
    d2 = abs(lst[i]-lst[1+i])
    if d1>=d2:
        print('False')
        break
    d1 = d2 
else:
    print('True')