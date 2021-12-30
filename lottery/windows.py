from PySimpleGUI import Window, Text, Output, Button, ProgressBar, WIN_CLOSED
from lottery.params import WELCOME_SENTENCES


def main_window(buttons):
    layout = [[Text('听风转转转酒吧2022年元旦抽奖晚会\n', font='黑体 47 bold')],
              buttons,
              [Button('败者食尘', button_color=('black', 'red'), key='-back-', disabled=True, font='黑体 12 bold')],
              [Text('操作记录', font='黑体 12 bold')],
              [Output(size=(120, 12), font='黑体 12')]]
    # layout = [[Text('Welcome to Tingfeng Lottery!')],
    #           buttons]
    return Window('小号茄子抽奖Robot v1.0', layout, finalize=True, icon='src/1.ico')


def show_text_window(sentences):
    max_len = max([len(s) for s in sentences]) * 2 + 5
    layout = [[Text('', font='黑体 12', key=f'-{i}-', size=(max_len, 1))] for i in range(len(sentences))] + \
             [[Button('下一幕', key='-next-', font='黑体 12', disabled=True)]]
    window = Window('', layout, finalize=True, icon='src/1.ico')
    process = [[0, len(s)] for s in sentences]
    while True:
        event, values = window.read(timeout=80)
        if event == WIN_CLOSED or event == 'EXIT' or event == '-next-':
            break
        for i in range(len(process)):
            if process[i][0] < process[i][1]:
                process[i][0] += 1
                window[f'-{i}-'].update(sentences[i][:process[i][0]])
                break
        if process[-1][0] == process[-1][1]:
            window['-next-'].update(disabled=False)
    window.close()


def show_process_bar(sentences, speed=1500):
    max_len = max([len(s) for s in sentences]) * 2
    layout = [[Text('', font='黑体 12', key='-t-')],
              [ProgressBar(len(sentences) * speed, orientation='h', size=(max_len, 20), key='-p-')]]
    window = Window('', layout, finalize=True, icon='src/1.ico')
    for i, s in enumerate(sentences):
        for j in range(speed):
            event, values = window.read(timeout=0, timeout_key='timeout')
            if event == WIN_CLOSED or event == 'EXIT':
                break
            window['-t-'].update(s)
            window['-p-'].update_bar(i * speed + j + 1)
    window.CloseNonBlocking()


def welcome_window():
    for sentences in WELCOME_SENTENCES[:-1]:
        show_text_window(sentences)
    show_process_bar(WELCOME_SENTENCES[-1])
