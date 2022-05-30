'''Write a Python program to count the combinations for non-consecutive 1's numbers patterns in a binary number string where the width of the binary given by the user.

for exmample 
n = 4
all binary string combinations at width 4
        0000
        0001
        0010
        0011
        0100
        0101
        0110
        0111
        1000
        1001
        1010
        1011
        1100
        1101
        1110
        1111

here non-consecutive 1's (consider char 0 is social distance) patterns are:
0001, 0010, 0100, 0101, 1000, 1001, 1010
total count of these patterns is 7'''

width = int(input())
count = 0
for i in range (1, 2**width):
    if '11' not in bin(i):
        count+=1
print(count)
        

    