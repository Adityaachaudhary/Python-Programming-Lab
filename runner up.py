#second largest character in string (using.replace that is a builtin function for string )
lst = 'hello'
mx = max(lst)
lst = lst.replace(mx,'')
mx = max(lst)
print('Maximum',mx)

#second largest element in lst
lst = [2, 4, 67, 23]
mx = max(lst)
