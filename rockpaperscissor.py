from random import randint

user_wins=0
computer_wins=0

options = ['rock','paper','scissor']

while True:
    user_pick=input("Enter rock,paper,scissor or q to exit")
    if user_pick=='q':
        break
    if user_pick not in options:
        continue
    
    b=randint(0,2)
    computer_pick = options[b]
    
    if user_pick=="rock" and computer_pick=="scissor":
        print(computer_pick)
        print("You Won")
        user_wins+=1
        continue
    elif user_pick=="paper" and computer_pick=="rock":
        print(computer_pick)
        print("You Won")
        user_wins+=1
        continue
    elif user_pick=="scissor" and computer_pick=="paper":
        print(computer_pick)
        print("You Won")
        user_wins+=1
        continue
    elif user_pick =="rock" and computer_pick=="rock":
        print(computer_pick)
        print("TIE")
        continue
    elif user_pick =="paper" and computer_pick=="paper":
        print(computer_pick)
        print("TIE")
        continue
    elif user_pick =="scissor" and computer_pick=="scissor":
        print(computer_pick)
        print("TIE")
        continue
    else:
        print(computer_pick)
        print("You Lost")
        computer_wins+=1
print("The Game Is Over")
print(f"You won {user_wins} times")
print(f"Computer won {computer_wins} times")