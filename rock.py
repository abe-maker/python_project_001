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
    if computerchoise == userinput:
        print("Tie!")
    
    if (computerchoise == "p" and userinput ==  "s") or (computerchoise == "r" and userinput == "p") or (computerchoise == "s" and userinput == "r"):
        print("You win!")
    else:
        print("You loose!")

    #print result
    print(f"Computer choose {computerchoise}")
    print(f"You choose {userinput}")
    
    #continue
    choice = input("Continue? (y/n): ").lower()
    if choice == "y":
        pass
    elif choice == "n":
        break
    else:
        print("Invalid input!")