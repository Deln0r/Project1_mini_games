from random import randint
from random import choice
RULES = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 10


def get_question_and_answer():
    n1 = randint(MIN_NUMBER, MAX_NUMBER)
    n2 = randint(MIN_NUMBER, MAX_NUMBER)
    operators = ['+', '-', '*']
    operator = choice(operators)
    question = f'{n1} {operator} {n2}'
    if operator == '+':
        corr_answer = n1 + n2
    elif operator == '-':
        corr_answer = n1 - n2
    elif operator == '*':
        corr_answer = n1 * n2
    return question, str(corr_answer)
