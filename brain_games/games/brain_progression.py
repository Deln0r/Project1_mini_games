from random import randint
RULES = 'What number is missing in the progression?'
MIN_RANDOM_INDEX = 0
MAX_RANDOM_INDEX = 9
MIN_FIRST_NUMBER = 1
MAX_FIRST_NUMBER = 15
MIN_STEP_SIZE = 2
MIN_STEP_SIZE = 5
ITEMS_IN_LIST = 10


def get_question_and_answer():
    a1 = randint(MIN_FIRST_NUMBER, MAX_FIRST_NUMBER)
    d = randint(MIN_STEP_SIZE, MIN_STEP_SIZE)
    random_index = randint(MIN_RANDOM_INDEX, MAX_RANDOM_INDEX)
    progression = make_progression(a1, d)
    corr_answer = progression[random_index]
    progression[random_index] = '..'
    question = " ".join(map(str, (progression)))
    return question, str(corr_answer)


def make_progression(a1, d):

    progression = [a1]
    for i in range(a1 + d, a1 + d * ITEMS_IN_LIST, d):
        progression.append(i)
    return progression
