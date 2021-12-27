import PySimpleGUI as sg
import random

datas = [['哈姐', '靛蓝之星*999'], ['五仁汤圆', '白化黑山羊角笛*1'], ['早苗', '莫莫拉·莫拉*1'],
         ['式部茉优', '香菜*99'], ['墨菲', '雇员幻想药*1'], ['风祭渔虎', '男Fur色图一套']]

gift_keys = [f'-{gift[1]}-' for gift in datas]
guys = [guy[0] for guy in datas]


def generate_buttons(datas):
    buttons = []
    for i in range(len(datas) // 5 + 1):
        buttons.append([sg.Button(gift[1], button_color=('white', 'black'), key=f'-{gift[1]}-', disabled=False)
                        for gift in datas[i*5:(i+1)*5]])
    return buttons


def make_window():
    layout = [[sg.Text('Welcome to Tingfeng Lottery!')],
              generate_buttons(datas),
              [sg.Text('Results'), sg.Output(size=(60, 15), font='Courier 8')]]
    return sg.Window('TFLottery', layout)


if __name__ == '__main__':
    window = make_window()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'EXIT':
            break
        if event in gift_keys:
            window[event].update(disabled=True)
            guy = random.choice(guys)
            print(f'Congrats!{guy} get {event[1:-1]}!')
            guys.remove(guy)
            window[event].update(disabled=True)

    window.close()
