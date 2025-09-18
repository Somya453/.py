import random

computer=random.randrange(1, 101)
player=int(input("Enter a number: "))


if player>computer:
    print("Computer number is", computer)
    print("Your guess number is high.")
    
elif computer>player:
    print("Computer number is", computer)
    print("Your guess number is too low")

else:
    print("Computer number is", computer)
    print("Your guess is right!")

 

