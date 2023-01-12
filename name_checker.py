name=input("Enter Your Name, Please: ")
if len(name) < 3:
    print("name must be 3 characters long")
elif len(name) > 50:
    print("name should be less than 50 characters long")
else:
    print("name looks good!")