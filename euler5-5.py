def LCM20(something):
    for i in range(1, 21):
        if something % i != 0:
            return False
    return True


something = 2520
while True:
    if LCM20(something):

something += 2520

print(something)