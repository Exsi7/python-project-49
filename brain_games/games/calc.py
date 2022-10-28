from random import randint, choice


game_task = 'What is the result of the expression?'


def random_operator():
    op = ['+', '-', '*']
    random_op = choice(op)
    return random_op


def expression(a, b, operator):
    if operator == '+':
        expression = a + b
    if operator == '-':
        expression = a - b
    if operator == '*':
        expression = a * b
    return expression


def calc():
    operator = random_operator()
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    question = (f'{random_number1} {operator} {random_number2}')
    exp = str(expression(random_number1, random_number2, operator))
    calculator = [question, exp]
    return calculator


calculator = [game_task, calc]
