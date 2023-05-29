from question_model import Question
from data import question_data

questionBank = []

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']

    data = Question(question_text, question_answer)

    questionBank.append(data)

print(questionBank)
