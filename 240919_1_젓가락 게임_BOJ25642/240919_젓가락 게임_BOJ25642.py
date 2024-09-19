# 젓가락 게임_BOJ25642

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, B = map(int, input().split())    # 용태와 유진이의 손가락 개수를 input 받고
flag = False                        # 공격 차례를 저장한 변수를 생성하고
while 1:                            # 종료될 때까지 반복해서
    if flag:                        # 유진이의 공격이라면
        A += B                      # 용태의 손가락에 유진이의 개수를 더하고
        flag = False                # 공격자를 변경한다
    else:                           # 용태의 공격이라면
        B += A                      # 유진이의 손가락에 용태의 개수를 더하고
        flag = True                 # 공격자를 변경한다
    if A >= 5:                      # 용태의 손가락이 5개를 넘었다면
        print('yj')                 # 유진이를 출력하고
        quit()                      # 종료한다
    elif B >= 5:                    # 유진이의 손가락이 5개를 넘었다면
        print('yt')                 # 용태를 출력하고
        quit()                      # 종료한다