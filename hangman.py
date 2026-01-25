import random

#word db
words = ["abc", "python", "himalayan", "jesus", "whitefield"]

#manage word
def manage_word(printword, letter):
    abcs = ["a", "b", "c"]
    abcs.remove(letter)
    for abc in abcs:
        printword = printword.replace(abc, "_")


#get user input and verarbeite it
def game(words):
    hangword = random.choice(words)
    printword = hangword.split(",")
    letter = input("letter? ")

    manage_word(printword, letter)
    print({printword})

game(words)
