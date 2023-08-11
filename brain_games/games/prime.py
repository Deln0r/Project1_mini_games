from random import randint
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def mechanics():
    n = randint(1, 100)
    corr_unswer = is_prime(n)
    question = n
    return question, corr_unswer


def is_prime(n):
    divider = 2
    while divider * divider <= n and n % divider != 0:
        divider += 1
    if divider * divider > n:
        return 'yes'
    else:
        return 'no'
