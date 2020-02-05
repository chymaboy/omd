# Guido van Rossum <guido@python.org>


def step1():
    print(
        'Уткамаляр 🦆 решила погулять. \n'
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        option = input('Выберите: {}/{}\n'.format(*options))

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print(
        'Отлично, ведь у утки коллекция зонтиков. \n'
        'Но какой выбрать? '
    )
    option = ''
    options = {'красный': 'red', 'синий': 'blue', 'зеленый': 'green'}
    while option not in options:
        option = input('Выберите: {}/{}/{}\n'.format(*options))

    if options[option] == 'red':
        return step3_red()
    elif options[option] == 'blue':
        return step3_blue()
    elif options[option] == 'green':
        return step3_green()


def step2_no_umbrella():
    print(
        'Пошел дождик и утка намокла. \n'
        'Спрятаться под гриб или поплавать в озере?'
    )
    option = ''
    options = {'гриб': True, 'озеро': False}
    while option not in options:
        option = input('Выберите: {}/{}\n'.format(*options))

    if options[option]:
        return step3_mushroom()
    return step3_lake()


def step3_mushroom():
    print(
        'Под грибом также спряталась другая уточка. \n'
        'Может быть, познакомиться с ней?'
    )
    option = ''
    options = {'крукнуть': True, 'молчать': False}
    while option not in options:
        option = input('Выберите: {}/{}\n'.format(*options))

    return step4_end()


def step3_lake():
    print(
        'В озере плавает и другая уточка. \n'
        'Может быть, познакомиться с ней?'
    )
    option = ''
    options = {'подплыть': True, 'уплыть': False}
    while option not in options:
        option = input('Выберите: {}/{}\n'.format(*options))

    return step4_end()


def step3_red():
    print(
        'Похоже, что красный зонт сломался. \n'
        'Надо выбрать другой.'
    )
    option = ''
    options = {'синий': 'blue', 'зеленый': 'green'}
    while option not in options:
        option = input('Выберите: {}/{}\n'.format(*options))

    if options[option] == 'blue':
        return step3_blue()
    elif options[option] == 'green':
        return step3_green()


def step3_blue():
    print(
        'Похоже, что синий зонт сломался. \n'
        'Надо выбрать другой.'
    )
    option = ''
    options = {'красный': 'red', 'зеленый': 'green'}
    while option not in options:
        option = input('Выберите: {}/{}\n'.format(*options))

    if options[option] == 'red':
        return step3_red()
    elif options[option] == 'green':
        return step3_green()


def step3_green():
    print(
        'Но только зеленый зонт не красиво. \n'
        'Какой аксессуар подобрать к нему?'
    )
    option = ''
    options = {'сумочка': 0, 'очечи': 1, 'галстук': 2}
    while option not in options:
        option = input('Выберите: {}/{}/{}\n'.format(*options))

    return step4_end()


def step4_end():
    print('Отлично. Но на землю упал метеорит и все умерли ☠️')


if __name__ == '__main__':
    step1()
