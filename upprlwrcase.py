def string_test(s):
    d={"UPPER_CASE":0,"LOWER_CASE":0}
    for c in s:
            if c.isupper():
                d["UPPER_CASE"]+=1
            elif c.islower():
                d["LOWER_CASE"]+=1
            else:
                pass
    print("original string :", s)
    print("nbr of upper case characters :", d["UPPER_CASE"])
    print("nbr of lower case characters :", d["LOWER_CASE"])
string_test('madarchod LUDOXX BHNkichutt TUMHARI')    
