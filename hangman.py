import random

#word db
words = ["abc", "python", "himalayan", "jesus", "whitefield"]

hangword = random.choice(words)
hiddenword = ["_" for _ in  hangword]


print("Welcome to Hangman!")

attemps = 8
print(f" ".join(hiddenword))
while attemps > 0 and "_" in hiddenword:
    
    guess = input("What is your guess?  ")
    if guess in hangword:
        for index,letter in enumerate(hangword):
            if guess == letter:
                hiddenword[index] = guess 
                
        print(f" ".join(hiddenword))
        print("Correct")
    else:
        print("Wrong letter")
    print("")
    attemps -= 1


