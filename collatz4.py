# André Roche  - Collatz Conjecture in Python. Wiki it on the Net

n = int(input("Please enter an interger:"))

i = 0

while n > 1:     # as long as n is greater than 1
    print (n)

    if n % 2 == 0:
        n = (n/2)
    print (n)
else: 
        n = (n*3 + 1)
        print (n)
i += 1
