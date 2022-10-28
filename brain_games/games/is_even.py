from random import randint


game_task = 'Answer \'yes\' if the number is even, otherwise answer \'no\'.'


def even():
    random_number = randint(1, 100)
    question = (f'{random_number}')
    if random_number % 2 == 0:
        exp = 'yes'
    if random_number % 2 == 1:
        exp = 'no'
    return [question, exp]


is_even = [game_task, even]
