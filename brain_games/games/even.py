from random import randint
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 10


def get_question_and_answer():
    question = randint(MIN_NUMBER, MAX_NUMBER)
    if is_even(question):
        corr_answer = 'yes'
    else:
        corr_answer = 'no'
    return question, corr_answer


def is_even(num):
    return num % 2 == 0
