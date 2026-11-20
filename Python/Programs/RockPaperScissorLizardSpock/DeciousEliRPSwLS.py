import random

#BELOW IS FOR ME SO I DO NOT MIXUP THE ORDER :)

'''
Rock beats Scissors and Lizard
Paper beats Spock and Rock
Scissors beats Lizard and Paper
Spock beats Rock and Scissors
Lizard beats Spock and Paper
'''
#simple intro
print("Hello this is my simple rock paper scissors app with rock paper scissors spock lizard additon!!! This was made by Eli Decious! I hope you enjoy my app!!!")

#Starts game mode. rps is rock paper scissors
gameMode = input("Tell me which mode you would like to play. Rock Paper Scissors(Type rps), or Rock Paper Scissors Spock Lizard? (Type rpssl)")
if gameMode == "rps":
    print("\n"*30) #just clears the screen
    print("You are playing Rock Paper Scissors")
    rpsChoice = int(input("Do you want to go Rock(0) Paper(1) or Scissors(2)?"))
    rpsList = ["rock","paper","scissors"] #List of rps choices
    r = random.choice(rpsList)
    print(f"The computer chose {r}")
#The list below was the only way ik how to make them compare. 100% sure theres a better way to do this but your way is wrong and mine is better so :)

#Winning conditions
    if r == "rock" and rpsChoice == 1:
        print("You quickly cover the computers rock with your paper!!!")
        print("HA! You win! The paper covered the rock and nobody can see it! And obviously, if you cannot see it it does not exist, therefore the paper is the last man standing!!")
    elif r == "paper" and rpsChoice == 2:
        print("You snip the computers paper into countless pieces!! How could you!?")
        print("You win! The paper is finely shredded and can no longer do anything!!")
    elif r == "scissors" and rpsChoice == 0:
        print("You smash the computers scissors against the ground with your rock")
        print("Yes! It worked!!! The scissors are in pieces you win!!")

#Losing condtions
    elif r == "rock" and rpsChoice == 2:
        print("The rock smashes your scissors against the ground!")
        print("Oh No!! The computer's rock smashed your scissors into thousands of pieces! You lost!!!")
    elif r == "paper" and rpsChoice == 0:
        print("The computer quickly covered your rock up with its paper! Where did it go!?")
        print("Oh No! The paper is hiding the rock so therefore it doesnt exist anymore!! You lost!!")
    elif r == "scissors" and rpsChoice == 1:
        print("The computer cuts your paper into pieces")
        print("Oh no!! The computer gave your paper a shredding and ruined it!! Your poor paper! You lost!")
    else:
        print(f"Uh oh! You guys both picked {r}! You two clash your {r}s out for an eternity and never win or lose!!! Stalemate computer stalemate!!!!!")
        print("The game was a tie")

elif gameMode == "rpssl":
    print("\n"*30) #just clears the screen
    print("You are playing Rock Paper Scissors Spock Lizard")
    rpsslChoice = int(input("Do you want to go Rock(0) Paper(1) Scissors(2) Spock(3) or Lizard(4)?"))
    rpsslList = ["rock","paper","scissors","spock","lizard"] #List of rpssl choices. Probably a better way than making a whole new list but...yk the saying
    rs = random.choice(rpsslList)
    print(f"The computer chose {rs}")
#The list below was the only way ik how to make them compare. 100% sure theres a better way to do this but your way is wrong and mine is better so :)

#Winning conditions (the player's pick beats the computer's pick)
    if rs == "rock" and rpsslChoice == 1:
        print("You quickly cover the computers rock with your paper!!!")
        print("HA! You win! The paper covered the rock and nobody can see it! And obviously, if you cannot see it it does not exist, therefore the paper is the last man standing!!")
    elif rs == "rock" and rpsslChoice == 3:
        print("Spock whips out his phaser and vaporizes the computers rock!!")
        print("Fascinating. The rock is now dust in the wind. You win!!")
    elif rs == "paper" and rpsslChoice == 2:
        print("You snip the computers paper into countless pieces!! How could you!?")
        print("You win! The paper is finely shredded and can no longer do anything!!")
    elif rs == "paper" and rpsslChoice == 4:
        print("Your lizard eats the computers paper!!")
        print("Nom nom nom. The lizard ate like a king!! You win!!")
    elif rs == "scissors" and rpsslChoice == 0:
        print("You smash the computers scissors against the ground with your rock")
        print("Yes! It worked!!! The scissors are in pieces you win!!")
    elif rs == "scissors" and rpsslChoice == 3:
        print("Spock smashes the computers scissors with pure logic and reasoning skills!!")
        print("The scissors are bent beyond repair. You win!!")
    elif rs == "spock" and rpsslChoice == 1:
        print("You hold up your paper to Spock's face and disprove him!!")
        print("He has no counter argument. The paper has the facts and he starts stumbling off. You win!!")
    elif rs == "spock" and rpsslChoice == 4:
        print("Your lizard poisons Spock!!")
        print("Spock may have been a genius but he never could find a cure for lizard poison!!! You win!!")
    elif rs == "lizard" and rpsslChoice == 0:
        print("You smash the lizards head with your rock!! You sick monster!!")
        print("You won but at what cost....rip lizard")
    elif rs == "lizard" and rpsslChoice == 2:
        print("You decapitate the computers lizard with your scissors!!")
        print("You are a terrible person!!! Why??? You get a dishonest victory!!")

#Losing conditions (the computer's pick beats the player's pick)
    elif rs == "rock" and rpsslChoice == 2:
        print("The rock smashes your scissors against the ground!")
        print("Oh No!! The computer's rock smashed your scissors into thousands of pieces! You lost!!!")
    elif rs == "rock" and rpsslChoice == 4:
        print("The computers rock beats your lizard over the head!!")
        print("Oh no!! Your poor lizard is now a dead lizard. You lost!! Shame on that commputer")
    elif rs == "paper" and rpsslChoice == 0:
        print("The computer quickly covered your rock up with its paper! Where did it go!?")
        print("Oh No! The paper is hiding the rock so therefore it doesnt exist anymore!! You lost!!")
    elif rs == "paper" and rpsslChoice == 3:
        print("The computers paper disproves Spock!!")
        print("Spock has no counter argument and sulks off. You lost!!")
    elif rs == "scissors" and rpsslChoice == 1:
        print("The computer cuts your paper into pieces")
        print("Oh no!! The computer gave your paper a shredding and ruined it!! Your poor paper! You lost!")
    elif rs == "scissors" and rpsslChoice == 4:
        print("The computers scissors decapitate your lizard!! How awful????")
        print("Oh no!! Your lizard has lost its head. You lost!! #JusticeForTheLizard")
    elif rs == "spock" and rpsslChoice == 0:
        print("Spock vaporizes your rock!!")
        print("Oh no!! Your rock....doesnt feel so good... You lost!!")
    elif rs == "spock" and rpsslChoice == 2:
        print("Spock smashes your scissors!!")
        print("Oh no!! Your scissors are bent beyond repair. You lost!!")
    elif rs == "lizard" and rpsslChoice == 3:
        print("The computers lizard bites and poisons Spock!!")
        print("Oh no!! Spock did not make it. You lost!!")
    elif rs == "lizard" and rpsslChoice == 1:
        print("The computers lizard ate your paper!!")
        print("Oh no!! Your paper is now lizard food. You lost!!")
    else:
        print(f"Uh oh! You guys both picked {rs}! You two clash your {rs}s out for an eternity and never win or lose!!! Stalemate computer stalemate!!!!!")
        print("The game was a tie")







































