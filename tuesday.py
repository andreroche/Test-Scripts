# André Roche - This is a test to see if it is tuesday

# Is it Tuesday?

import datetime # this is importing a library

if datetime.datetime.today().weekday() == 1: # this is just a format taken from stack overflow on the net
    print("yay! It is Tuesday.")
else:
    print("Unfortunately it is not Tuesday") 

