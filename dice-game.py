import random
for _ in range(1000):
    firstnumber = random.randint(1, 6)
    secondnumber = random.randint(1, 6)

    choose = input("Roll the dice? (y/n): ")

    if choose == "y":
        a = firstnumber
        b = secondnumber
        print(f"{a}, {b}")
        


    elif choose == "n":
        print("Thanks for playing!")

    else:
        print("Invalid choise!")
    print("")
    


