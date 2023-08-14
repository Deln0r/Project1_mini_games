from random import randint
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def get_question_and_answer():
    question = randint(MIN_NUMBER, MAX_NUMBER)
    if is_prime(question):
        corr_unswer = 'yes'
    else:
        corr_unswer = 'no'
    return question, corr_unswer


def is_prime(n):
    divider = 2
    if n == 1:
        return False
    while divider * divider <= n and n % divider != 0:
        divider += 1
    if divider * divider > n:
        return True
    else:
        return False
