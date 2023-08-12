import prompt
ROUNDS = 3


def play(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES)
    for round in range(ROUNDS):
        question, corr_answer = game.mechanics()
        print(f"Question: {question}")
        answer = prompt.string('Your answer: ')
        if corr_answer == answer:
            print('Correct!')
        else:
            f'\"{answer}\" is wrong answer ;(.'
            f' Correct answer was "{corr_answer}".'
            print(f'Let\'s try again, {name}!')
            break
    else:
        print(f'Congratulations, {name}!')
