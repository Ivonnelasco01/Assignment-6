import random
questions = {}
score = 0
print("Math Quiz")

def quiz(n):
    for i in range(10):
        int_a = random.randint(0,99)
        int_b = random.randint(0,99)
        operator = ("+")
        question = str(int_a)+" "+(operator)+" "+str(int_b)
        answer = eval(question)
        question += " = "

        questions.update({question: str(answer)})
quiz(10)
for q in questions.keys():
    user_answer = input(q)
    if questions.get(q) == str(user_answer):
        score+=1
        print("Correct")
    else:
        print("Incorrect")

print("Result: "+str(score)+"/10")