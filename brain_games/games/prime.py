from random import randint
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def mechanics():
    n = randint(1, 100)
    corr_unswer = is_prime(n)
    question = n
    return question, corr_unswer


def is_prime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    if d * d > n:
        return 'yes'
    else:
        return 'no'
