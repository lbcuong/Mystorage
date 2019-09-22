import random


characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
def createPw():
    while True:
        user = input("Generating password, Do you want a weak(enter 1) or a strong(enter 2) password? \n")
        if user == '1':
            password = ''.join(random.sample(characters, 2))
            print(password)
            break
        elif user == '2':
            password = ''.join(random.sample(characters, 10))
            print(password)
            break
        else:
            print("Please try again!")

createPw()
while True:
    print("Do you want to change password? (Y|N)")
    user = input()
    if user == 'Y':
        createPw()
    elif user == 'N':
        break
    else:
        print("Please type again")

