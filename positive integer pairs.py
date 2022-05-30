'''WAP for given integer p and x that displays the positive integer pairs (i,j) which satisfy the following 
condition:- i+j = p and i^j =x'''



def check(x,y):
    for i in range (0,x):
        j = x-i
        if j^i == y :
            return i,j
    
        
P = int(input())
X = int(input())
out = check(P,X)
print(out[0],out[1])
