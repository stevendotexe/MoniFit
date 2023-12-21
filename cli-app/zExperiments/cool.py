def coolStuff():
    from time import sleep
    from math import sin, cos
    x = 1
    y = 1
    for _ in range(40):
        y += 3
        x += .1
        print(' ' * (int(abs(sin(y) * 69))), '|')

        sleep((int(abs(cos(x) * 69)))/3000)