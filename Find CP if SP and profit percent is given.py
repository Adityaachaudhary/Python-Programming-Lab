#write a python program to calculate the cost price of the product and selling price is entered by user having a profit margin of 15%
SP = int(input('Enter the Selling Price of the product:'))
CP = 100*SP/(100+15)
print("the cost price of the product is INR", CP)

