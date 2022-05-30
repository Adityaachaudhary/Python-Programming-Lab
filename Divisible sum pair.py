'''Given an array of integers and a positive numbers of (i,j) pairs when i<j and ar[i]+ar[j] is divisible by k
ex:- ar = [1,2,3,4,5,6] 
     k = 5
     three pairs meet the  criteria: [1,4],[2,3] and [4,6]
     so output is 3'''

def dsp(n,k,arr):
    count = 0
    for i in range(n):
        for j in range (i+1, n):
            if (arr[i] + arr[j] % k ==0):
                count += 1
    return count
        

n,k = list(map(int, input().split))
arr = list(map(int, input().split()))
out = dsp(n,k,arr)
print(out)