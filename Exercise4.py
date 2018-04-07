# André Roche  - Project Euler Problem 5   24-Feb-18. More info @ https://projecteuler.net/problem=5
# Reference https://thecodeaddict.wordpress.com/2011/10/29/project-euler-005/ for base code 
# Prime Numbers referenced at http://www.prime-numbers.net/prime-numbers-1-20-chart.html 
# Least Common Multiple referenced at https://www.quora.com/Whats-the-LCM-of-1-2-3-4-5-6-7-8-9-10-How-to-get-it 
# Break Statement reference pages 320, 389 and 391 Learning Python 5th Edition
# Booleans learned at pages 171/172 & 304 Learning Python 5th Edition 

def lcm(something):                            # Declare/Create my own function to call later. 'something' is the argument.
    for x in range (11,21):                    # Numbers in range 11-20 used for speed. As per problem statement, 1-10 LCM is known already. No need to repeat.
        if something % x != 0:                 # If the remainder of the 'something' when divided by the numbers in the range 11-20 is not equal to 0 i.e. not evenly divisible.
            return False                       # Return false or a '0' if the condition above is true i.e something is not evenly divisible by 11-20 . See Booleans page 171/172 & 304 Learning Python 5th Edition.
    return True                                # Return true or a int '1' if condition something % x == 0 i.e something is evenly divisble by 11-20.
something = 2520                               # Counter. Starting at 1 takes too long (don't try it :-)) ,1-10 is established as is 2520 so we can start at this number. 
while True:                                    # When the condition is true or a '1'. It's a loop where the condition is true.
    if lcm(something):                         # Start of if statement. If this is True, you've found 'something' i.e the smallest number evenly divisable by 11-20
        break                                  # Statement to exit the loop - see page 320 Learning Python 5th Edition.
    something += 2520                          # Counter = Counter + 2520. This number is used for speed. 1-10 LCM = 2520 so 2520 must be a divisor of the number i'm trying to find. 

    print(something)                           # Print to screen the value incremented in steps of 2520 until you find the number evenly divisible by 11-20.Then it breaks the loop.

print("The LCM of numbers 1-20 is", something) # Outside the loop, print the final number with a text instruction before the number.
