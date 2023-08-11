import math
from random import randint
RULES = 'Find the greatest common divisor of given numbers.'


def mechanics():
    n1 = randint(1, 50)
    n2 = randint(1, 50)
    question = f'{n1} {n2}'
    corr_answer = str(math.gcd(n1, n2))
    return question, corr_answer
