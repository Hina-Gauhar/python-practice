# guessing game

print("welcome to game")
print("u have 3 attempts ")
choice=1
import random

guess_num=random.randint(1,100)
# guess_num=13
while(choice<4):
    user=int(input("guess the number: "))
    if(user>guess_num):
        print("come lower")
        choice+=1
    elif(user<guess_num):
        print("go a bit higher")
        choice+=1
    else:
        print("u r correct that is the number")
        break   
else:
    print("Try again")
    
