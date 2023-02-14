# a dictionary that stores questions and answers
# have a variable that tracks the score of the player
# loop through the dictionary using the key value pairs
# display each question to the user and allow them to answer
# tell them if they are right or wrong
# show the final result when quiz is completed

quiz = {
    "question 1": {
        "question": "What is the capital of France?",
        "answer" : "Paris"
    },
    "question 2":{
        "question": "What is the capital of Germany?",
        "answer" : "Berlin"
    },
    "question 3":{
        "question": "What is the capital of Italy?",
        "answer" : "Rome"
    },
    "question 4":{
        "question": "When did India gain Independence?",
        "answer" : "1945"
    },
    "question 5":{
        "question": "Who is the President of USA?",
        "answer" : "Joe Biden"
    },
    "question 6":{
        "question": "How many continents are there on Earth?",
        "answer" : "7"
    },
    "question 7":{
        "question": "Who is the founder of Tesla?",
        "answer" : "Elon Musk"
    },

}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer?")

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score + 1
        print("Your score is: " + str(score))
        print("")
        print("")

    else:
        print("Wrong!")
        print("The answer is :" +value['answer'])
        print("Your score is:" + str(score))
        print("")
        print("")

print("You got " + str(score) + " out of 7 questions correctly")
print("Your percentage is " + str(int(score/7 * 100))+ "%")
