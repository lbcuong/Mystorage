import random

number = random.randint(1,9)
count = 0
guess = 0
while True:
    try:    
        guess = input("Enter your guess number: ")

        if guess == "exit":
            print("Finishing the game!")
            break
        else:
            if int(guess) == number:
                print("exactly right")
                print("You guessed totally:", count, "time")
                break
            elif int(guess) < number:
                print("too low")
            else:
                print("too high")

        count += 1
    except:
        print("Incorrect")
        continue


        
