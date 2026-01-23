questions = [
    {"prompt": "Which city is the Capital of France?", "options": "A:Bourdeaux, B:Cannes, C:Paris, D:Marssailes", "answer": "C"}, 
    {"prompt": "Whats the best country of africa?","options": "A:Nigeria, B:Mozambique, C:Uganda, D:South Africa", "answer":"D"}, 
    {"prompt": "Whats the coolest motorcycle?", "options": "A: Royal Enfield Himalayan 411, B: Triumph Bonneville 900, C: Yamaha MT-09, D: Honda Rebel 750", "answer": "B"}
]

#print question and userinput
def asking_question(question):
    print(f"{question["prompt"]}")
    userinput = input(f"{question["options"]}   Answer: ").upper()
    return userinput


#checking result
def checking_result(userinput, rightanswer, score):
    if userinput == rightanswer:
        print("")
        print(f"Correct! The right answer is {rightanswer}")
        score = score + 1
        return score
    else:
        print(f"Wrong! The right answer is {rightanswer}")
        return
    


def quiz(questions):
    score = 0
    for question in questions:
        userinput = asking_question(question)
        rightanswer = question["answer"]
        
        score = checking_result(userinput, rightanswer, score)
        print("")

    print(f"Game Over! Your score is {score}")
    print("")




quiz(questions)
