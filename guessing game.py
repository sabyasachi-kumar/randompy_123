secret_num=6
i=0
counter=0
while i<3:
    guess=int(input("enter your guess: "))
    if guess==secret_num:
       print("Congratulations,You win!")
       counter=1
       break
    else:
        if i<2:
         print("try again!")
    i=i+1
if counter==0:
    print("Sorry, You Loose!")

