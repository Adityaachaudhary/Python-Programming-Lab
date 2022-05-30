st = input()
node = int(input())
rep = int(input())

print(*(st[node:] + st[:node]).replace(' ','')*rep)