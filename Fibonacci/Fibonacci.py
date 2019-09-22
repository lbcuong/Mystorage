print("Fibonacci Range")
def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    elif number == 2:
        return 1
    elif number == 3:
        return 2
    else:
        return fibonacci(number-1) + fibonacci(number-2)
while True:
    user = int(input("Enter the amount of number: "))
    for number in range(0, user):
        print(fibonacci(number))
    while True:
        print("Do you want to continue (Y|N): ")
        user = input()
        if user == 'Y':
            continue
        elif user == 'N':
            break
        else:
            print("Wrong, type again")
        
