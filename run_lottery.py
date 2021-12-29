from lottery.windows import main_window, welcome_window
from lottery.utils import gift_parser, generate_gift_buttons, list_gifts
from lottery.params import GIFTS_INFO, GUYS
from PySimpleGUI import WIN_CLOSED, theme
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
            guy = choice(REST_GUYS)
            GIFTS[event[1:-1]].giftee = guy
            list_gifts(GIFTS[event[1:-1]])
            REST_GUYS.remove(guy)
            window[event].update(disabled=True)
            GIFTS_NUM[GIFTS[event[1:-1]].tab] -= 1
            PROCESS_STACK.append((guy, event))
            window['-back-'].update(disabled=False)
        if event == '-back-':
            guy, key = PROCESS_STACK.pop(-1)
            REST_GUYS.append(guy)
            GIFTS[key[1:-1]].giftee = ''
            window[key].update(disabled=False)
            GIFTS_NUM[GIFTS[key[1:-1]].tab] += 1
            if not PROCESS_STACK:
                window['-back-'].update(disabled=True)
            print(f'发动败者食尘！【{guy}】回到候选名单，并复原奖项【{key[1:-1]}】\n')
