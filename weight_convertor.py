weight=int(input("Enter Your Weight, Please: "))
unit=input("(L)bs or (K)g: ")
if unit=="L" or unit=="l":
    print("Your Weight in kg is: ", weight/2.205)
elif unit=="K" or unit=="k":
    print("Your weight in pound is: ", weight*2.205)
else:
    print("Unit entered is wrong")