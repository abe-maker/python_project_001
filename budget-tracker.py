#welcome
print("Welcome to the Budget App")
budget = input("Please enter you budget: ")


#objects
remainingbudget = budget
expenses = {}
totalspend = 0

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
        expense = input("Enter your expense description: ").title()
        amount = input("Wnter expense amount: ")
        expenses[expense] = amount
        totalspend = totalspend + int(expenses[expense])
        remainingbudget = int(remainingbudget) - int(expenses[expense])
        print(f"Added expense: {expense}, Amount: {amount}")

    elif option == "2":
        print(f"Total Budget: {budget}")
        print("Expenses")
        for key, value in expenses.items():
            print(f"- {key}: {value}")
        print(f"Total Spend: {totalspend}")
        print(f"Remaining Budget: {remainingbudget}")

    elif option == "3":
        break

