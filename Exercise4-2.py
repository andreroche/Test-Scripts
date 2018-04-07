# André Roche  - Project Euler Problem 5   24-Feb-18. More info @ https://projecteuler.net/problem=5
def gcd(a, b) :
    if a == 0: return b
    if b == 0: return a
    if a < 0:  a = -a
    if b < 0:  b = -b
 
    while b != 0:
        a, b = b, a%b
    return a
 
result = 2
for i in range(2,21) :
    result = i / gcd(result,i) * result
print (result)                                 

   