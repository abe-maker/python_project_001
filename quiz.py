questions = [
    {"prompt": "Which city is the Capital of France?", "options": "A:Bourdeaux, B:Cannes, C:Paris, D:Marssailes ", "answer": "C"},
]

#print question and userinput
def asking_question(question):
    print(f"{question("prompt")}")
    userinput = input(f"{question("options")}")
    return userinput


#checking result
def checking_result(userinput, rightanswer, score):
    if userinput == rightanswer:
        print(f"Correct! The right answer is {rightanswer}")
        score = score + 1
        return True
    else:
        print(f"Wrong! The right answer is {rightanswer}")
        return False


def quiz(questions):
    for question in questions:
        userinput = asking_question(question)
        rightanswer = questions("answer")
        score = 0
        checking_result(userinput, rightanswer, score)

    print(f"Games Over! Your score is {score}")




quiz(questions)
