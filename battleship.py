import _utf8
_utf8.main()

from random import randint

board = []

for i in range(5):
    board.append(['O']*5)

def 보드출력(board):
    for row in board:
        print(' '.join(row))

보드출력(board)

sr, sc = randint(0,4), randint(0,4)             #컴퓨터의 배 좌표

count = int(5 * 5 * 0.25)
while count > 0:
    print('남은 시도횟수:',count)
    try:
        L = input('x,y로 입력:').split(',')        #사용자 입력
        gr, gc = int(L[0]), int(L[1])
    except:
        print('잘못된 입력. 다시 입력해 주세요')
        continue

    if sr == gr and sc == gc:
        print('승리')
        break
    else:
        if gr not in range(5) or gc not in range(5):
            print('범위를 벗어난 공격입니다')
        elif board[gr][gc] == 'X':
            print('같은 곳을 또 포격')
        else:
            print('꽝')
            board[gr][gc] = 'X'
            보드출력(board)

        count-=1
else:
    print('ㅋㅋㅋㅋㅋㅋ')

print('game over')


#--------------------------------------------------------------------------

'''board = []
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
coin = 1
life = 1
count = 1
csx, csy = randint(0,a-1), randint(0,a-1)             #컴퓨터의 배 좌표
print(csx+1,csy+1)
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
        print('컴퓨터는 {},{}를 포격했다!'.format(cy+1,cx+1))

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
        print('같은y인듯 하다!')
    elif ux == csx and csy != uy:
        print('같은x인듯 하다!')

    컴퓨터보드판(c_board)
    print('\n')
    보드출력(board)'''
