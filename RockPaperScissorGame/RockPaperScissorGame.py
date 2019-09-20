import random

def rockPaperScissor():
    computer = ['rock', 'paper', 'scissor']
    while True:
        user = input("Your selection is: ")
        computerSelection= random.choice(computer)
        print("Computer selection :", computerSelection)
        if ((user == 'rock') or (user == 'paper') or (user == 'scissor')):
            if user == 'rock':
                if computerSelection == 'paper':
                    print("You lose!!!")
                elif computerSelection == 'scissor':
                    print("You win!!!")
                else:
                    print("Drawwwww")
            if user == 'paper':
                if computerSelection == 'scissor':
                    print("You lose!!!")
                elif computerSelection == 'rock':
                    print("You win!!!")
                else:
                    print("Drawwwww")
            if user == 'scissor':
                if computerSelection == 'rock':
                    print("You lose!!!")
                elif computerSelection == 'paper':
                    print("You win!!!")
                else:
                    print("Drawwwww")
            break
        else:
            print("Incorrect")

rockPaperScissor()

while True:
    print("Do you want to play a new game? Y|N")
    answer = input()
    if answer == 'Y':
        print("Start a new game!")
        rockPaperScissor()
    elif answer == 'N':
        break
    else:
        print("Please type Y or N")
            
        

  
