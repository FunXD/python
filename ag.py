import _utf8
_utf8.main()

import random
rock = 1
sissers = 2
paper = 3

def is_playing_stop():
    _a_str = input("더 하시겠습니까? (y/n)")
    if _a_str.lower().startswith('n'):
        return True
    else:
        return False
        count = 0

def who_win():
    eq = me - com
    if eq == 0:
        print ('No Win')
    elif eq == 1 or eq == -2:
        print ('You Lose')
    elif eq == -1 or eq == 2:
        print ('Win')

while True:
    print('바위=1 가위=2 보=3')
    me = (int(input("어떤것을 내시겠습니까? ")))
    com = random.randint(1,3)
    print(com)
    who_win()
    stop_okay = is_playing_stop()       \안녕
    if stop_okay:
        break
    print('\n')
