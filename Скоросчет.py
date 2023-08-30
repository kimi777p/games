import datetime
import random

coins = 0
application = 1
time = datetime.datetime.now()

true = True
while true:
    var1 = random.randint(0, 10)
    var2 = random.randint(0, 10)
    application = random.randint(1, 2)
    if application == 1:
        result = input(var1+'+'+var2)
        if result == format(var1 + var2):
            print('yes')
            coins += 1
        else:
            print('no')
            coins -= 1
    if application == 2:
        result = input(var1+'-'+var2)
        if result == format(var1 - var2):
            print('yes')
            coins += 1
        else:
            print('no')
            coins -= 1
    print('your count: '+coins)
    exit = input('if you want to exit, press(enter), else press(space)')
    if exit == '':
            true = False
