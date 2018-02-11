# André Roche  - Collatz Conjecture in Python. Wiki it on the Net

n = int(input("Please enter an interger: "))
  if n%2 == 0:
    n = n/2
    print (n)
  else:
    n = 3*n+1
    print (n)
i+=1
