import json 

with open('questions.json', 'r') as file:
    content = file.read()

data = json.loads(content)

score = 0

print("Welcome to this MCQ Test!")

for i, question in enumerate(data):
    print("Question ", i+1, ":", sep="")
    print(data[i]["question_text"])
    for j, alternative in enumerate(data[i]["alternatives"]):
        print(j+1, ": ", alternative, sep="")
    
    user_ans = int(input("Select the most appropriate alternative: "))
    if user_ans == data[i]["correct"]:
        score += 1

print("\n\nEnd of Quiz\n")

for i in range(len(data)):
    print("Question: ", data[i]["question_text"], sep="")
    print("Correct Option: ", data[i]["alternatives"][data[i]["correct"]-1], sep="")
    print("Your Answer: ", data[i]["alternatives"][user_ans-1], "\n", sep="")


print("Your score is ", score, "/", len(data), sep="")
