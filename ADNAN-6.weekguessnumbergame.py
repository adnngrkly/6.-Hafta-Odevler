print("Please hold on your brain a number between 0 and 100")

import random
value=random.randint(0,100)
valuel=[0,100]
while True:
    print("your guess number:{}".format(value))
    choose=input("The number, more than you know - , less than you know +  or equal == :\t")
    if choose=="+":
        valuel.sort()
        valuel.pop(0)
        valuel.append(value)
        valuel.sort()
        value = random.randint(valuel[0], valuel[1])
        continue
    elif choose == "-":
        valuel.sort()
        valuel.pop(1)
        valuel.append(value)
        valuel.sort()
        value = random.randint(valuel[0], valuel[1])
        continue
    elif choose=="==":
        print("you kew it")
        quit()
    else:
        print("You enter wrong value,Please you try again")
        continue