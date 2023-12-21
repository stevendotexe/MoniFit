def coolStuff():
    from random import choice
    from termcolor import cprint
    from time import sleep
    from math import sin, cos
    x = 1
    y = 1
    for _ in range(40):
        y += 3
        x += 0.1

        selected_color = choice(['red', 'green', 'blue'])
        print_this = ' ' * int(abs(sin(y) * 69)) + '|'
        cprint(print_this, selected_color)

        sleep(int(abs(cos(x) * 69)) / 3000)