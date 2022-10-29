from random import randint


game_task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime():
    random_number = randint(1, 100)
    divisor = 1
    exp = 'yes'
    while divisor < random_number:
        if random_number % divisor == 0 and divisor != 1:
            exp = 'no'
            break
        divisor = divisor + 1
    return [random_number, exp]


prime = [game_task, is_prime]
