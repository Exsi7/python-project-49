from random import randint


game_task = 'What number is missing in the progression?'


def create_progression():
    random_len = randint(5, 10)
    random_element = randint(1, 50)
    progression_dif = randint(1, 10)
    progression = []
    while random_len > 0:
        progression.append(random_element)
        random_element = random_element + progression_dif
        random_len = random_len - 1
    return progression


def game():
    progress = create_progression()
    lenght = len(progress) - 1
    random_index = randint(0, lenght)
    question = []
    question.extend(progress)
    question[random_index] = '..'
    exp = str(progress[random_index])
    return [question, exp]


progression = [game_task, game]
