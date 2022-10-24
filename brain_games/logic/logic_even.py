from random import randint


def is_even():
    print('Welcome to the Brain Games')
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print('Hello, ' + name)
    score = 0
    while score < 3:
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        print('Your answer:', end='')
        answer = input()
        if random_number % 2 == 1 and answer == 'no':
            print('Correct!')
            score = score + 1
        elif random_number % 2 == 0 and answer == 'yes':
            print('Correct!')
            score = score + 1
        elif random_number % 2 == 1 and answer == 'yes':
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print("Let's try again, " + name)
            break
        elif random_number % 2 == 0 and answer == 'no':
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            print("Let's try again, " + name)
            break
    else:
        print(f'Congratulations, {name}!')
