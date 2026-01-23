import random

#user input
while True:
    while True:
        userinput = input("Rock, paper, or scissors? (r/p/s): ").lower()
        print("")
        if userinput == "r" or userinput == "p" or userinput == "s":
            break
        else:
            print("Invalid choice")


    #computer choise
    computerchoices = ["r", "p", "s"]
    computerchoise = random.choice(computerchoices)

    #computer choice assignement
    values = { "r": "Dawye the Rock Johnson", "p": "Paper", "s": "Scissor"}

    #lose or win
    if computerchoise == userinput:
        print("Tie!")
    
    elif (computerchoise == "p" and userinput ==  "s") or (computerchoise == "r" and userinput == "p") or (computerchoise == "s" and userinput == "r"):
        print("You win!")
    else:
        print("You loose!")

    #print result
    print(f"Computer choose {values[computerchoise]}")
    print(f"You choose {values[userinput]}")
    print("")
    
    #continue
    while True:
        choice = input("Continue? (y/n): ").lower()
        if choice == "y":
            continue
        elif choice == "n":
            break
        else:
            print("Invalid input!")
            continue