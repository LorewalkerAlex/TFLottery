from PySimpleGUI import Window, Text, Output, Button


def main_window(buttons):
    layout = [[Text('Welcome to Tingfeng Lottery!')],
              buttons,
              [Button('BACK', button_color=('black', 'red'), key='-back-', disabled=True)],
              [Text('Results'), Output(size=(100, 15))]]
    # layout = [[Text('Welcome to Tingfeng Lottery!')],
    #           buttons]
    return Window('TFLottery', layout)

