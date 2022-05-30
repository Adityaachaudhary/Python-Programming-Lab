st = list(input())

while 1:
    ln = len(st)
    for i in range (ln-1):
        if st[i] == st[i+1]:
            st.pop(i)
            st.pop(i)
            break

    else:
        st= ''.join(st)
        print(st if st else 'Empty String')
        break
    
 