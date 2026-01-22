import random

#generating number
number = random.randint(1, 100)

#user input
while True:
    usernum = input("Guess the number between 1 and 100: ")

    if int(usernum) == number:
        print("Congratulations! You guessed the number.")
        break

    elif int(usernum) < number:
        print("Too low!")
    
    elif int(usernum) > number:
        print("Too high!")
