x = 10
if x > 5:
    print("x is greater than 5")


x = 2
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")


x = 10
if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")


x = 15
if x > 10:
    print("Above 10")
    if x > 20:
        print("Also above 20")
    else:
        print("But not above 20")


age = 20
if age >= 18 and age < 60:
    print("Adult")
else:
    print("Not an adult or senior")
