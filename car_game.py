quit=0
car_status=0
while quit==0:
    command=input(">")
    command=command.lower()
    if command=="help":
       print("start - start the car")
       print("stop - stop the car") 
       print("quit  - exit")
    elif command=="start":
        if car_status==1:
            print("car already started")
        elif car_status==0:
            print("car started...ready to go!")
            car_status=1
    elif command=="stop":
        if car_status==0:
            print("car is already stopped")
        elif car_status==1:
            print("car is stopped")
            car_status=0
    elif command=="quit":
        quit=1
    else:
        print("I don't understand that")