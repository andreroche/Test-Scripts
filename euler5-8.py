euler5_Answer = False 
x=2520

while not euler5_Answer:
    x+=2520
    for y in range(2,21):
        if x%y != 0:
            break
    else:
        euler5_Answer = x
print (euler5_Answer)


