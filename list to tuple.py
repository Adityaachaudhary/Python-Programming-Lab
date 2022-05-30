list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

tup = [(list1[i], list2[i]) for i in range(0, len(list1))]

print(tup)