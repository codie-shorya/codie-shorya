import random

random_number=random.randint(1,30)
userguess =None
guess=0

while (userguess!=random_number):
    userguess=int(input("enter the number:"))
    guess += 1
    if userguess==random_number:
        print("you guessed the number right")
    else:
        print("you guessed the number wrong\n")
        if userguess>random_number:
            print("the guessing number is smaller than yours number\n")
        else :
            print("the guessing number is larger than yours number\n")

print(f"the number of your guess is {guess}\n")
with open('highscore.txt')as f:
    hiscore=int(f.read())

if hiscore>guess:
    print("Bravo! you just broke the current highscore")
    with open('highscore.txt','w') as f:
        f.write(str(guess))
