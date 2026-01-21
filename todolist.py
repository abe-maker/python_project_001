todos = []

for _ in range(1000):

    print("was willst du tun?")
    print("(1) Liste anzeigen")
    print("(2) Element hinzufügen")
    print("")
    choose = input("Auswahl: ")

    if float(choose) == 1:
        print("")
        print("Liste:")
        for todo in todos:
            print(f"- {todo}")
        print("")

    
    if float(choose) == 2:
        print("")
        newitem = input("Was soll ich hinzufügen? ")
        todos.append(newitem)

