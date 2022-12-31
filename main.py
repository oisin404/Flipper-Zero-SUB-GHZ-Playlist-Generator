def currecnyChange():
    currecy = input("What currency would you like to exchange? ")
    price = float(input("How much would you like to exchange? "))
    if currecy == "usd":
        print(price * 1.15)
    elif currecy == "yen":
        print(price * 7)
    else:
        print("Please input a valid currency.")
        currecnyChange()

currecnyChange()