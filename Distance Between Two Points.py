#write a python script to calculate the distance between 2 points in X-Y plane
#    .________________________.
# (x1,x2)<---------D-------->(y1,y2)

x1 = int(input('enter the value of x1:'))
x2 = int(input('enter the value of x2:'))
y1 = int(input('enter the value of y1:'))
y2 = int(input('enter the value of y2:'))

D = (((x2-x1)**2)+((y2-y1)**2))**0.5
print("the distance between two points is", D,"unit")


