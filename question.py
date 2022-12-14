import os
import json
from pprint import pprint

class Question:
    def __init__(self, text, image, answers, correct_answer):
        self.text = text
        self.image = image
        self.answers = answers
        self.correct_answer = correct_answer        
    def __repr__(self):
        return "Question: " + self.text + "\nAnswers: " + str(self.answers) + "\nRight answer: " + str(self.correct_answer)
        
def checkSpelling(question):
    for answer in question.answers:
        if answer[0] == question.correct_answer:
            return True
    return False

def checkUpperCase(question):
    for answer in question.answers:
        if answer[0][:1].isalpha():
            answer[0] =answer[0][:1].upper() + answer[0][1:]
        if question.correct_answer[:1].isalpha():
            question.correct_answer = question.correct_answer[:1].upper() + question.correct_answer[1:]
        

def loadQuize(path):
        questions = []
        quize = json.load(open("./" + path + "/content.json", encoding='utf-8'))
        for quest in quize["questions"]:
                q = Question(quest["text"], quest["image"], quest["answers"], quest["correct_answer"])
                checkUpperCase(q)
                if not checkSpelling(q):
                    print("Error in question")
                    print(q)
                    exit()
                                    
                questions.append(q)
        print("Quize successfully loaded!" + "\nThere are " + str(len(questions)) + " questions...")
        return questions
