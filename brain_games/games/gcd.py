import math
from random import randint
RULES = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 50


def get_question_and_answer():
    n1 = randint(MIN_NUMBER, MAX_NUMBER)
    n2 = randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{n1} {n2}'
    corr_answer = str(math.gcd(n1, n2))
    return question, corr_answer
