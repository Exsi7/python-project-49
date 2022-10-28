def engine_game(game):
    print('Welcome to the Brain Games')
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print('Hello, ' + name)
    print(game[0])
    score = 0
    while score < 3:
        game_operation = game[1]()
        print(f'Question: {game_operation[0]}')
        print('Your answer:', end='')
        answer = input()
        if answer == game_operation[1]:
            print('Correct!')
            score = score + 1
        else:
            print(f'\'{answer}\' is wrong answer ;(.'
                  f'Correct answer was \'{game_operation[1]}\'')
            print("Let's try again, " + name)
            break
    else:
        print(f'Congratulations, {name}!')
