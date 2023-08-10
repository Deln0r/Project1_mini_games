from random import randint
from random import choice
RULES = 'What is the result of the expression?'


def mechanics():
    n1 = randint(1, 10)
    n2 = randint(1, 10)
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
