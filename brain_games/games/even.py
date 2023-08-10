from random import randint
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def mechanics():
    question = randint(1, 100)
    if question % 2 == 0:
        corr_answer = 'yes'
    else:
        corr_answer = 'no'
    return question, corr_answer
