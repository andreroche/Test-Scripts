def factorial(f):
    if f == 0:
        return 1
    else:
        return f * factorial(f-1)

while True:
    f = input('Input a number to compute the factorial: ')
    if f.isdigit():
        break

f=int(input("Input a number to compute the factorial : "))


print(factorial(f))


print("The factorial for 5 should be 120, The result is : ", factorial(5))
print("The factorial for 7 should be 5040, The result is : ", factorial(7))
print("The factorial for 10 should be 3628800, The results is : ", factorial(10))