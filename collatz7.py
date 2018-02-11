# GMIT Python  -----  André Roche 09-Feb-2018
# Collatz Conjecture Test Script ----- References for while, if and else statements taken from course videos. X counter taken from www.stackoverflow.com 

n = int(input("Please enter an interger: ")) # ask the user on screen to enter an integer 
x = 0             # start counter
print (n)         # print the value of n to screen - this will be the first number entered by the user
while n > 1:      # assuming n is greater than 1 because a user might enter 0 or 1
 if n % 2 == 0:   # if n divided by 2 leaves no remainder i.e it's even
    n = n/2       # then n = n divided by 2 
    print (n)     # print the value of n to the screen
 else:            # if it's not the above i.e. it's not an even number
    n = 3*n+1     # then n = n multiplied by 3 plus 1
    print (n)     # print the value of n to the screen
x = x + 1         # counter = counter +1 

print ("The final value of N is:" , n) # This line is not necessary, just using it to confirm the sequence ends at 1
