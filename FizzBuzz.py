# André Roche  - FizzBuzz game in Python. Wiki FizzBuzz on the Net

i = 1

while i <= 100:     # as long as i is less than or equal to 100
  if (i % 3 == 0) and (i % 5 == 0): # if the remiander of i divided by 3 is 0 and i divided by 5 is 0 then print FizzBuzz
    print ("FizzBuzz")
  elif i % 3 == 0: # else if only i divided by 3 is 0 print Fizz
    print ("Fizz")
  elif i % 5 ==0: # else if only i divided by 5 is 0 print Buzz
    print ("Buzz")
  else:   # if it's neither of the above, i.e. neither division by 3 or 5 leaves a remainder of 0 then just print the value of i
    print (i)
  i = i + 1     # standard command to ensure i increments
