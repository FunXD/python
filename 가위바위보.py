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
        print ('무승부')
    elif eq == 1 or eq == -2:
        print ('패배')
    elif eq == -1 or eq == 2:
        print ('승리')

while True:
    print('바위=1 가위=2 보=3')
    me = (int(input("어떤것을 내시겠습니까? ")))
    com = random.randint(1,3)
    if com == 1:
        print('상대방은 바위를 냈다')
    elif com ==2:
        print('상대방은 가위를 냈다')
    else:
        print('상대방은 보자기를 냈다')
    print(com)
    who_win()
    stop_okay = is_playing_stop()       #안녕
    if stop_okay:
        break
    print('\n')
