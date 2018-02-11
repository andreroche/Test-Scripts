# André Roche  - Collatz Conjecture in Python. Wiki it on the Net

n = 27 

while n <= 27:
    if n % 2 == 0:
        print (n / 2)
    else:
        print (n*3 +1)
