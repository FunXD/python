#10204 박준하

import _utf8
_utf8.main()

from random import randint

name = input('당신의 이름은?')

while True:
    n=int(input('난이도를 선택하세요(쉬움:1 어려움:2)'))
    if n !=1 and n!=2:
        print('잘못된 입력')
        continue
    else:
        break
coin = 1
life = 1
com_win = 0
player_win = 0

def 게임시작():
    global life, coin
    board = []
    c_board = []                                            #computer_board
    while True:                                             #판 크기
        a=int(input('판의 크기는?(5~12) '))
        if a in range(5,13):
            break
        else:
            print('잘못된 입력')
            continue

    for i in range(a):
        board.append(['O']*a)
        c_board.append(['O']*a)

    def 보드출력(board):
        for row in board:
            print(' '.join(row))

    def 컴퓨터보드판(c_board):
        for row in c_board:
            print(' '.join(row))

    count = 1
    csx, csy = randint(0,a-1), randint(0,a-1)             #컴퓨터의 배 좌표
    #print(csx+1,csy+1)
    while True:
        try:
            L = input('{}의 배의 좌표는?(x,y로 입력)'.format(name)).split(',')     #사용자의 배 좌표
            usy, usx = int(L[0])-1, int(L[1])-1             # 'user ship x' 'user ship y'
            if usy>a-1 or usx>a-1 or usx<0 or usy<0:
                print('벗어난 범위')
                continue
            print('--------------------------')
            break
        except:
            print('잘못된 입력. 다시 입력해 주세요')
            continue

    while count >= 0:
        try:
            print('\n')
            L = input('{}은(는) 어디를 포격할까? (x,y로 입력)'.format(name)).split(',')        #사용자 포격 입력
            ux, uy = int(L[0])-1, int(L[1])-1
            if uy>a-1 or ux>a-1:
                print('벗어난 범위')
                continue
            print('--------------------------','\n')
        except:
            print('잘못된 입력. 다시 입력해 주세요')
            continue

        for i in range(n):
            cx, cy = randint(0,a-1), randint(0,a-1)         #컴퓨터 포격 입력

            while True:
                cx, cy = randint(0,a-1), randint(0,a-1)
                if not board[cx][cy] =='X':
                    break
            print('컴퓨터는 {},{}를 포격했다!'.format(cy+1, cx+1))

            if cx == usx and cy == usy:                     #컴퓨터 적중 여부s=x
                print('맞았다!!', '\n')
                life = 0
            else:
                board[cx][cy] ='X'
                print('그러나 공격은 빗나갔다!', '\n')

        if life == 0:
            break

        if uy == csy and ux == csx:                             #사용자 적중 여부
            print(name,'은(는) {},{}를 포격했다!'.format(ux+1,uy+1))
            print('효과는 굉장했다!')
            c_board[ux][uy] = 'X'
            컴퓨터보드판(c_board)
            print('\n')
            보드출력(board)
            break
        else:
            if uy not in range(a) or ux not in range(a):
                print('범위를 벗어난 공격입니다')
            elif c_board[ux][uy] == 'X':
                print('같은 곳을 또 포격했다!')
            else:
                print(name,'은(는) {},{}를 포격했다!'.format(ux+1,uy+1))
                print('그러나 공격은 빗나갔다!', '\n')
                c_board[ux][uy] = 'X'

        count+=1

        if csy == uy and ux != csy:
            print('같은 y인듯 하다!')
        elif ux == csx and csy != uy:
            print('같은 x인듯 하다!')

        컴퓨터보드판(c_board)
        print('\n')
        보드출력(board)

while True:
    coin = 1
    life = 1
    게임시작()
    if life == 1:
        print('\n','you win!')
        player_win +=1
    else:
        print('\n','game over')
        com_win +=1
    print('----------------------','\n','현재 스코어는 {} 대 {} 입니다'.format(player_win,com_win))
    coin = int(input(('다시하시겠습니까? (y=1 n=0)')))
    if coin !=1 and coin !=0:
        print('잘못된 입력')
        continue
    elif coin == 0:
        break
    else:
        print('----------------------')
        continue
