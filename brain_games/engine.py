import prompt


def play(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES)
    for round in range(3):
        question, corr_answer = game.mechanics()
        print(f"Question: {question}")
        answer = prompt.string('Your answer: ')
        if corr_answer == answer:
            print('Correct!')
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{corr_answer}".')
            print(f'Let\'s try again, {name}!')
            break
    else:
        print(f'Congratulations, {name}!')
