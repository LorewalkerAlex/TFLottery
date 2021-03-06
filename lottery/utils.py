from collections import defaultdict
from PySimpleGUI import Button, Tab, TabGroup


class Gift:

    def __init__(self, name, num, gifter):
        self.name = name
        self.num = num
        self.gifter = gifter


class GiftPakage:

    def __init__(self, pkg_name, tab_name):
        self.name = pkg_name
        self.tab = tab_name
        self.gifts = []
        self.giftee = ''

    def set_giftee(self, giftee):
        self.giftee = giftee

    def add_gift(self, gift):
        self.gifts.append(gift)


def gift_parser(gift_info):
    gift_d = defaultdict(list)
    gifts = dict()
    for gift_part in gift_info:
        for pkg_name in gift_info[gift_part]:
            gpkg = GiftPakage(pkg_name, gift_part)
            for single_gift in gift_info[gift_part][pkg_name]:
                gpkg.add_gift(Gift(*single_gift))
            gifts[pkg_name] = gpkg
            gift_d[gift_part].append(gpkg)
    return gift_d, gifts, {gift_part: len(gift_d[gift_part]) for gift_part in gift_d}


def generate_gift_buttons(gifts_d):
    tabs = []
    for gift_part in gifts_d:
        tabi_layout = []
        for i in range(len(gifts_d[gift_part]) // 5 + 1):
            tabi_layout.append([Button(gpkg.name, button_color=('white', 'black'), key=f'-{gpkg.name}-',
                                       disabled=False, font='黑体 12')
                                for gpkg in gifts_d[gift_part][i*5:(i+1)*5]])
        tabs.append(Tab(f'{gift_part}({len(gifts_d[gift_part])})', tabi_layout, key=f'-{gift_part}-'))
    return [[TabGroup([tabs], font='黑体 14 bold')]]


def list_gifts(gpkg):
    print(f'【{gpkg.giftee}】获得了【{gpkg.name}】')
    print(f'【{gpkg.name}】包含如下奖品：')
    for gift in gpkg.gifts:
        print(f'由【{gift.gifter}】赠送的【{gift.name}*{gift.num}】')
    print('\n')
