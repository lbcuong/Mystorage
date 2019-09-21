import random

number = random.randint(1,9)
count = 0
guess = 0
while True:
    guess =input("Enter your guess number: ")

    if guess == "exit":
        print("Finishing the game!")
        break
    else:
        print("Incorrect")
        continue

    guess = int(guess)
    count += 1

    if guess == number:
        print("exactly right")
        print("You guessed totally:", count, "time")
        break
    elif guess < number:
        print("too low")
    else:
        print("too high")
        
