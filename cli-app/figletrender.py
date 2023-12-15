from pyfiglet import Figlet

def figlet_render(text, font='drpepper'):
    fig = Figlet(font = font)
    return fig.renderText(text)