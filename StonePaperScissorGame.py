import random
lst=['s', 'p' , 'sr']

chance=5
no_of_chance=0
computer_point=0
your_point=0

print("\n .............. Stone , Paper , scissor game ..............\n \n  ")
print("s for stone \n p for paper \n sr for sissor \n \n ")

while no_of_chance < chance:
    _input = input("Stone , paper , scissor : ")
    _random = random.choice(lst)
    # print(_random)

    if _input == _random:
        print("Tie !! , No Point ")

    elif _input == "s" and _random == "p":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n ")
        print("Computer Wins 1 point \n ")
        print(f"Computer_point is {computer_point} and your point is {your_point} \n ")

    elif _input == "s" and _random == "sr":
        your_point = your_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n ")
        print("You Win 1 point \n ")
        print(f"Computer_point is {computer_point} and your point is {your_point} \n ")

    elif _input == "p" and _random == "s":
        your_point = your_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n ")
        print("You Win 1 point \n ")
        print(f"Computer_point is {computer_point} and your point is {your_point} \n ")

    elif _input == "p" and _random == "sr":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n ")
        print("Computer Wins 1 point \n ")
        print(f"Computer_point is {computer_point} and your point is {your_point} \n ")

    elif _input == "sr" and _random == "s":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n ")
        print("Computer Wins 1 point \n ")
        print(f"Computer_point is {computer_point} and your point is {your_point} \n ")

    elif _input == "sr" and _random == "p":
        your_point = your_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n ")
        print("You Win 1 point \n ")
        print(f"Computer_point is {computer_point} and your point is {your_point} \n ")

    else:
        print("Your input is wrong !!")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n ")

print("Game Over !")
if computer_point > your_point :
    print("Computer Wins and you loose :( ")

if computer_point < your_point:
    print("Congrats !! , You win the game :) ")

print(f"your point is {your_point} and computer point is {computer_point}")







