def test_prime(n):
    for i in range (2,n):
        if n%i==0:
            print("prime")
            break
    else:
        print("not prime")
test_prime(77)
        