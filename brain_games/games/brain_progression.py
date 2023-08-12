from random import randint
RULES = 'What number is missing in the progression?'


def mechanics():
    start = randint(1, 15)
    step = randint(2, 5)
    rand_index = randint(0, 9)
    progression = [start]
    for i in range(start+step, start+step*10, step):
        progression.append(i)
    corr_answer = progression[rand_index]
    progression[rand_index] = '..'
    question = " ".join(map(str, (progression)))
    return question, str(corr_answer)
