from lottery.windows import main_window, welcome_window
from lottery.utils import gift_parser, generate_gift_buttons, list_gifts
from lottery.params import GIFTS_INFO, GUYS
from PySimpleGUI import WIN_CLOSED, theme, popup_yes_no, popup_auto_close
from random import choice


GIFTS_D, GIFTS, GIFTS_NUM = gift_parser(GIFTS_INFO)
REST_GUYS = GUYS.copy()
PROCESS_STACK = []


if __name__ == '__main__':
    theme('Light Purple')
    welcome_window()
    window = main_window(generate_gift_buttons(GIFTS_D))
    while True:
        for tab in GIFTS_NUM:
            window[f'-{tab}-'].update(f'{tab}({GIFTS_NUM[tab]})')
        event, values = window.read()
        if event == WIN_CLOSED or event == 'EXIT':
            break
        if event[1:-1] in GIFTS:
            if popup_yes_no(f'你确定封印【{event[1:-1]}】？\n封印内容：\n' +
                            ''.join([f'来自【{gift.gifter}】的【{gift.name}*{gift.num}】\n'
                                     for gift in GIFTS[event[1:-1]].gifts]),
                            button_color=('black', 'red'), font='黑体 12 bold', icon='src/1.ico') == 'Yes':
                guy = choice(REST_GUYS)
                GIFTS[event[1:-1]].giftee = guy
                list_gifts(GIFTS[event[1:-1]])
                REST_GUYS.remove(guy)
                window[event].update(disabled=True)
                GIFTS_NUM[GIFTS[event[1:-1]].tab] -= 1
                PROCESS_STACK.append((guy, event))
                window['-back-'].update(disabled=False)
            else:
                popup_auto_close('这么大一个按钮您都能点错？', button_color=('black', 'red'), font='黑体 12 bold', icon='src/1.ico')
        if event == '-back-':
            if popup_yes_no(f'你确定使用杀手皇后败者食尘能力？\n' +
                            f'发动这能力后，【{PROCESS_STACK[-1][1][1:-1]}】将被解封，而【{PROCESS_STACK[-1][0]}】会毫不知情的回到上一个时间点',
                            button_color=('black', 'red'), font='黑体 12 bold', icon='src/1.ico') == 'Yes':
                guy, key = PROCESS_STACK.pop(-1)
                REST_GUYS.append(guy)
                GIFTS[key[1:-1]].giftee = ''
                window[key].update(disabled=False)
                GIFTS_NUM[GIFTS[key[1:-1]].tab] += 1
                if not PROCESS_STACK:
                    window['-back-'].update(disabled=True)
                print(f'发动败者食尘！【{guy}】回到候选名单，并复原奖项【{key[1:-1]}】\n')
            else:
                popup_auto_close('由于受到了欧拉欧拉欧拉，boki了', button_color=('black', 'red'), font='黑体 12 bold', icon='src/1.ico')
