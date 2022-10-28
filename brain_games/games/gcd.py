from random import randint


game_task = 'Find the greatest common divisor of given numbers.'


def gcd():
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    question = (f'{random_number1} {random_number2}')
    if random_number1 >= random_number2:
        gcd = random_number2
    else:
        gcd = random_number1

    while random_number1 % gcd != 0 or random_number2 % gcd != 0:
        gcd = gcd - 1
    exp = str(gcd)
    return [question, exp]


gcd_game = [game_task, gcd]
