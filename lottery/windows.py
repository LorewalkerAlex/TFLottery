from PySimpleGUI import Window, Text, Output, Button, ProgressBar


def main_window(buttons):
    layout = [[Text('听风转转转酒吧2022年元旦抽奖晚会\n', font='黑体 47 bold')],
              buttons,
              [Button('败者食尘', button_color=('black', 'red'), key='-back-', disabled=True, font='黑体 12 bold')],
              [Text('操作记录', font='黑体 12 bold')],
              [Output(size=(120, 12), font='黑体 12')]]
    # layout = [[Text('Welcome to Tingfeng Lottery!')],
    #           buttons]
    return Window('TFLottery', layout, finalize=True)


def welcome_window():
    layout = [[Text('')]]