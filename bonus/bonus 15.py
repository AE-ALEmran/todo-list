import json

with open("question.json", 'r') as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index+1, "-", alternative)
    user_action = int(input("Enter your answer :"))
    question["user_action"] = user_action

score = 0
for index, question in enumerate(data):
    if question["user_action"] == question["correct_ans:"]:
        score = score+1
        result =  "Correct Answer"
    else:
        result = "Wrong Answer"
    message = (f"{index+1} {result}-Your Answer :{question['user_action']} "
               f"Correct Answer :{question ['correct_ans:']}")
    print(message)

print("Your Score is :", score)