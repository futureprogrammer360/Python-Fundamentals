import json
import random
import os
import time

def read_data():
    with open("quiz.json", "r") as file:
        data = json.load(file)
    return data

def question(data):
    print("Question " + str(data["id"]))
    print(data["question"])

    random.shuffle(data["choices"])
    options = ["A", "B", "C", "D"]
    choices = {options[i]: data["choices"][i] for i in range(len(data["choices"]))}
    for option, choice in choices.items():
        print(" " + option + ". " + str(choice))

    answer = input("Your answer: ")
    if choices.get(answer.upper()) == data["answer"] or answer.lower() == str(data["answer"]).lower():
        print("Correct!")
        return 1
    else:
        print("Incorrect, the correct answer is " + str(data["answer"]))
        return 0

def main():
    os.system("cls")

    total = 0
    correct = 0

    data = read_data()
    for i in range(len(data)):
        correct += question(data[i])
        total += 1
        time.sleep(1)
        os.system("cls")

    print("You got " + str(correct) + " out of " + str(total))

main()
