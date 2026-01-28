#welcome
print("Welcome to the Budget App")
budget = input("Please enter you budget: ")


#objects
remainingbudget = budget
expenses = {}


#do loop
while True:
    print("")
    print("What would you like to do?")
    print("1. Add an expense")
    print("2. Show budget")
    print("3. Exit")
    option =  input("Enter you choice: ").strip()
    print("")

    if option == "1":
        expense = input("Enter your expense description: ")
        amount = input("Wnter expense amount: ")
        expenses[expense] = amount
        print(f"Added expense: {expense}, Amount: {amount}")

    

# adding


#anzeigen