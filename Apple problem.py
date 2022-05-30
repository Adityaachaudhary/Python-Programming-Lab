num = 1
while 1:
        if num %7 ==0 and num % 60 ==1:
            print(num)
            break
        num += 1
        
# for second number
num = 1
count = 0
while 1:
        if num %7 ==0 and num % 60 ==1:
            print(num)
            count +=1
            if count >=2:       
                 break
        num += 1