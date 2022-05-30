phonebook = {}
num = int(input())
for i in range (num):
    name,mobile = input().split
    phonebook [name] =mobile   

for i in range (num):
    query = input()
    res = phonebook.get(query)
    if res:
        print(f'{query}=res')
    else:
        print('Not Found')
        