from lottery.windows import main_window
from lottery.utils import gift_parser, generate_gift_buttons, list_gifts
from lottery.params import GIFTS_INFO, GUYS
from PySimpleGUI import WIN_CLOSED
from random import choice


GIFTS_D, GIFTS = gift_parser(GIFTS_INFO)
REST_GUYS = GUYS.copy()
PROCESS_STACK = []


if __name__ == '__main__':
    window = main_window(generate_gift_buttons(GIFTS_D))
    while True:
        event, values = window.read()
        if event == WIN_CLOSED or event == 'EXIT':
            break
        if event[1:-1] in GIFTS:
            guy = choice(REST_GUYS)
            GIFTS[event[1:-1]].giftee = guy
            list_gifts(GIFTS[event[1:-1]])
            REST_GUYS.remove(guy)
            window[event].update(disabled=True)
            PROCESS_STACK.append((guy, event))
            window['-back-'].update(disabled=False)
        if event == '-back-':
            guy, key = PROCESS_STACK.pop(-1)
            REST_GUYS.append(guy)
            window[key].update(disabled=False)
            if not PROCESS_STACK:
                window['-back-'].update(disabled=True)
            print(f'Something goes wrong, put {guy} back and refresh{key[1:-1]}')
