salary=int(input('enter your salary'))
if salary>1000:
    print('I will eat japanese')
    if salary>5000:
        print('3 star resturant')
        if True:
            print('false')
    elif salary>10000:
        print('5 star resturant')
    else:
        print('street stall')
elif salary>500:
    print('I will eat chinese')
elif salary>100:
    print('I will eat Dosa')
else:
    print('I will eat cookies')
