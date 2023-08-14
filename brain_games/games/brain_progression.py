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
    RANDOM_INDEX = randint(MIN_RANDOM_INDEX, MAX_RANDOM_INDEX)
    progression = make_progression()
    corr_answer = progression[RANDOM_INDEX]
    progression[RANDOM_INDEX] = '..'
    question = " ".join(map(str, (progression)))
    return question, str(corr_answer)


def make_progression():
    start = randint(MIN_FIRST_NUMBER, MAX_FIRST_NUMBER)
    step = randint(MIN_STEP_SIZE, MIN_STEP_SIZE)
    progression = [start]
    for i in range(start + step, start + step * ITEMS_IN_LIST, step):
        progression.append(i)
    return progression
