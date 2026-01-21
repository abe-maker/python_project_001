import random

#user input
while True:
    while True:
        userinput = input("Rock, paper, or scissors? (r/p/s): ").lower()
        if userinput == "r" or userinput == "p" or userinput == "s":
            break
        else:
            print("Invalid choice")


    #computer choise
    compnum = random.randint(1,3)
    if compnum == 1:
        computerchoise = "r"
    
    elif compnum == 2:
        computerchoise = "p"

    elif compnum == 3:
        computerchoise = "s"


    #lose or win
    if computerchoise == "r":
        if userinput == "r":
            print("you choose r")
            print("Computer choose r")
            print("Tie!")
        elif userinput == "p":
            print("you choose p")
            print("Computer choose r")
            print("you win!")
        elif userinput == "s":
            print("you choose s")
            print("Computer choose r")
            print("you Loose!")

    elif computerchoise == "p":
        if userinput == "r":
            print("you choose r")
            print("Computer choose p")
            print("you loose!")
        elif userinput == "p":
            print("you choose p")
            print("Computer choose p")
            print("Tie!")
        elif userinput == "s":
            print("you choose s")
            print("Computer choose ")
            print("you win!")

    elif computerchoise == "s":
        if userinput == "r":
            print("you choose r")
            print("Computer choose s")
            print("you win!")
        elif userinput == "p":
            print("you choose p")
            print("Computer choose s")
            print("you loose!")
        elif userinput == "s":
            print("you choose s")
            print("Computer choose s")
            print("Tie!")
    
    
    #continue
    choice = input("Continue? (y/n): ").lower()
    if choice == "y":
        pass
    elif choice == "n":
        break
    else:
        print("Invalid input!")